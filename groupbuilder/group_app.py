from threading import Thread

import wx
from time import sleep

from groupbuilder.algorithm_thread import RoundWorkerThread
from groupbuilder.core import GroupConfig
from .layout.layout_base import AppFrame
from .csv_name_picker_dialog import NameDialog
from .file_picker_dialog import FilePickDialog
from .group_config_dialog import GroupConfigDialog

from .utility.number_to_text import number_to_column
from .utility.grid_export import export_grid_to_csv

class GroupApp(AppFrame):
    def __init__(self, parent):
        super(GroupApp, self).__init__(parent)
        self.csv_pick_dialog: NameDialog | None = None
        self.csv_name_dialog: FilePickDialog | None = None
        self.group_config_dialog: GroupConfigDialog | None = None
        self.csv_path: str | None = None
        self.csv_data: list[list] | None = None
        self.csv_has_header: bool | None = None
        self.csv_name_index: int | None = None
        self.csv_surname_index: int | None = None
        self.csv_cancel: bool = False

        self.group_config_cancel: bool = False
        self.person_size: int | None = None
        self.group_size: int | None = None

        self.grid_data: dict[int, str] | None = None
        self.rounds: list[list[frozenset[int]]] | None = None

        self.paused: bool = False
        self.worker_running: bool = False
        self.worker_thread: RoundWorkerThread | None = None

        self.generated_rounds_number: int = 0
        self.max_rounds_number: int = 0
        self.current_round: int = 0

        self.status_text_ctrl.SetValue("Stopped")
        self.pause_button.Enable(False)
        self.round_progress_text_ctrl.SetValue("0 / 0")
        self.grid.SetColLabelValue(0, "Gruppenzuordnung")
        self.grid.SetColLabelValue(1, "Person")

    def on_close( self, event ):
        self.stop_worker_thread()
        event.Skip()

    def on_round_selector_enter( self, event ):
        if not self.rounds:
            self.round_selector_tctrl.SetValue("1")
            wx.MessageBox("Es wurden noch keine Runden generiert!", "Fehler", wx.OK | wx.ICON_ERROR)
            event.Skip()
            return
        try:
            page = int(self.round_selector_tctrl.GetValue())-1
        except ValueError:
            self.round_selector_tctrl.SetValue(str(self.current_round + 1))
            wx.MessageBox("Bitte eine Zahl eingeben!", "Fehler", wx.OK | wx.ICON_ERROR)
            event.Skip()
            return
        if page > len(self.rounds) or page < 0:
            self.round_selector_tctrl.SetValue(str(self.current_round + 1))
            wx.MessageBox("Die Runde existiert nicht!", "Fehler", wx.OK | wx.ICON_ERROR)
            event.Skip()
            return
        self.render_grid(page)
        event.Skip()

    def on_csv_load_button_click( self, event ):
        self.stop_worker_thread()
        self.csv_path = None
        self.csv_data = None
        self.csv_has_header = None
        self.csv_name_index = None
        self.csv_surname_index = None
        self.grid_data = None

        self.grid.ClearGrid()

        self.csv_pick_dialog = FilePickDialog(self)
        self.csv_pick_dialog.ShowModal()
        if self.csv_cancel:
            self.csv_cancel = False
            event.Skip()
            return

        self.csv_name_dialog = NameDialog(self)
        self.csv_name_dialog.ShowModal()
        if self.csv_cancel:
            self.csv_cancel = False
            event.Skip()
            return

        if self.csv_has_header:
            self.csv_data = self.csv_data[1:]
        if not self.csv_name_index is None and not self.csv_surname_index is None:
            self.grid_data = {i: f"{row[self.csv_name_index]} {row[self.csv_surname_index]}" for i, row in enumerate(self.csv_data)}
        elif not self.csv_name_index is None and self.csv_surname_index is None:
            self.grid_data = {i: row[self.csv_name_index] for i, row in enumerate(self.csv_data)}
        elif not self.csv_surname_index is None:
            self.grid_data = {i: row[self.csv_surname_index] for i, row in enumerate(self.csv_data)}
        else:
            self.grid_data = {i: f"Person {i + 1}" for i in range(len(self.csv_data))}
        self.group_config_dialog = GroupConfigDialog(self, len(self.csv_data), True)
        self.group_config_dialog.ShowModal()
        if self.group_config_cancel:
            self.group_config_cancel = False
            event.Skip()
            return
        self.start_worker_thread()
        event.Skip()

    def on_gconfig_button_click( self, event ):
        self.stop_worker_thread()
        self.group_config_dialog = GroupConfigDialog(self)
        self.group_config_dialog.ShowModal()
        if self.group_config_cancel:
            self.group_config_cancel = False
            event.Skip()
            return
        self.grid_data = {i: f"Person {i + 1}" for i in range(self.person_size)}
        self.start_worker_thread()
        event.Skip()

    def on_pause_button_click( self, event ):
        if self.worker_thread is None:
            event.Skip()
            return
        self.status_text_ctrl.SetValue("Bitte warten...")
        self.pause_button.Enable(False)
        if self.paused:
            self.worker_thread.resume()
        else:
            self.worker_thread.pause()
        event.Skip()

    def on_csv_export_change( self, event ):
        export_grid_to_csv(self.grid, event.GetPath())
        event.Skip()

    def OnSize( self, event ):

        total_width = self.GetClientSize().GetWidth() - 10  # 10 is a magic number / the border width of the grid
        num_cols = self.grid.GetNumberCols()
        col_width = total_width // num_cols

        for col in range(num_cols):
            self.grid.SetColSize(col, col_width)

        self.grid.Layout()

        if event:
            event.Skip()

    def start_worker_thread(self):
        from .algorithm_thread import RoundWorkerThread
        if not self.worker_running:
            self.rounds = []
            self.worker_running = True
            # 'self.algorithm' is an instance of GroupingAlgorithm
            self.worker_thread = RoundWorkerThread(self,
                                                   GroupConfig(amount_people=self.person_size, group_size=self.group_size))
            self.worker_thread.daemon = True
            self.worker_thread.start()

    def on_round_generated(self, round_data, round_number, max_rounds, paused: bool):
        # Update UI with 'round_data'
        # Then if needed, start the next round or stop the thread
        self.rounds.append(round_data)
        self.generated_rounds_number = round_number
        self.max_rounds_number = max_rounds
        self.round_selector_tctrl.SetMax(round_number)

        self.round_progress_text_ctrl.SetValue(f"{round_number} / {max_rounds}")
        self.update_status(paused)

    def update_status(self, paused: bool):
        self.paused = paused
        if self.worker_running:
            self.pause_button.Enable(True)

        if not self.worker_running:
            self.status_text_ctrl.SetValue("Stopped")
        elif paused:
            self.status_text_ctrl.SetValue("Paused")
        elif not self.paused:
            self.status_text_ctrl.SetValue("Running")

    def render_grid(self, page: int):
        if self.grid_data is None or self.rounds is None:
            return
        if page > len(self.rounds) or page < 0:
            return
        self.grid.DeleteRows(0, self.grid.GetNumberRows())
        self.grid.InsertRows(0, self.person_size)

        current_page = self.rounds[page]
        person_index = 0
        for i, group in enumerate(current_page):

            group_str = f"Gruppe {page + 1}{number_to_column(i + 1)}"
            for n, person in enumerate(group):
                person = f"{self.grid_data[person]}"
                self.grid.SetCellValue(person_index, 0, group_str)
                self.grid.SetCellValue(person_index, 1, person)
                person_index += 1
        self.grid.Refresh()
        self.grid.Layout()

    def setup_status(self):
        self.status_text_ctrl.SetValue("Setting up...")
        self.pause_button.Enable(False)
        self.round_progress_text_ctrl.SetValue("0 / 0")
        self.grid.ClearGrid()
        self.current_round = 0
        self.round_selector_tctrl.SetValue("1")

    def stop_worker_thread(self):
        if self.worker_thread is not None:
            self.worker_thread.stop()
            self.worker_thread.join(2)
            self.worker_thread = None
            self.worker_running = False
            self.status_text_ctrl.SetValue("Stopped")
            self.pause_button.Enable(False)
            self.round_progress_text_ctrl.SetValue("0 / 0")


if __name__ == '__main__':
    app = wx.App()
    frame = GroupApp(None)
    frame.Show()
    app.MainLoop()
