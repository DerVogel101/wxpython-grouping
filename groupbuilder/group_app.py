"""
Group App Module
==============

This module provides the main application class for the Group Builder application.

.. inheritance-diagram:: groupbuilder.group_app
   :parts: 1

.. autosummary::
   :toctree: generated/

   GroupApp
"""

import wx

from groupbuilder.algorithm_thread import RoundWorkerThread
from groupbuilder.core import GroupConfig
from .layout.layout_base import AppFrame
from .csv_name_picker_dialog import NameDialog
from .file_picker_dialog import FilePickDialog
from .group_config_dialog import GroupConfigDialog

from .utility.number_to_text import number_to_column
from .utility.grid_export import export_grid_to_csv

class GroupApp(AppFrame):
    """
    Main application class for the Group Builder application.

    This class handles the user interface, CSV data import/export,
    group configuration, and interaction with worker threads for group generation.

    .. inheritance-diagram:: groupbuilder.group_app.GroupApp
       :parts: 1

    .. autosummary::
       :toctree: generated/

       __init__
       on_close
       on_round_selector_enter
       on_csv_load_button_click
       on_gconfig_button_click
       on_pause_button_click
       on_csv_export_change
       OnSize
       start_worker_thread
       on_round_generated
       update_status
       render_grid
       setup_status
       stop_worker_thread
    """
    def __init__(self, parent):
        """
        Initialize the GroupApp.

        Sets up the application's initial state, including UI components,
        data structures, and state variables for CSV handling, group configuration,
        and worker thread management.

        :param parent: Parent window
        :type parent: wx.Window
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
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

    def on_close(self, event):
        """
        Handle window close event by stopping any running worker threads.

        Ensures clean shutdown by stopping any active worker threads before
        the application window closes.

        :param event: The close event
        :type event: wx.CloseEvent
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        self.stop_worker_thread()
        event.Skip()

    def on_round_selector_enter(self, event):
        """
        Handle round selection input events.

        Validates and processes user input in the round selector control,
        ensuring the selected round exists before updating the display.

        :param event: The event triggered when entering a value in the round selector
        :type event: wx.CommandEvent
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
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

    def on_csv_load_button_click(self, event):
        """
        Handle CSV load button click events.

        Implements the workflow for loading person data from a CSV file:
        1. Show file picker dialog
        2. Show column selection dialog
        3. Show group configuration dialog
        4. Start worker thread with the configured data

        :param event: The button click event
        :type event: wx.CommandEvent
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
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

    def on_gconfig_button_click(self, event):
        """
        Handle group configuration button click events.

        Opens a dialog for configuring groups without CSV data,
        then starts the worker thread with the specified configuration.
        Uses generic person names (Person 1, Person 2, etc.) instead of CSV data.

        :param event: The button click event
        :type event: wx.CommandEvent
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
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

    def on_pause_button_click(self, event):
        """
        Handle pause button click events.

        Toggles the pause state of the worker thread, providing
        visual feedback in the UI about the current state.

        :param event: The button click event
        :type event: wx.CommandEvent
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
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

    def on_csv_export_change(self, event):
        """
        Handle CSV export file selection events.

        Exports the current grid data to the selected CSV file path
        when the user selects a destination file.

        :param event: The file selection event
        :type event: wx.FileDirPickerEvent
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        export_grid_to_csv(self.grid, event.GetPath())
        event.Skip()

    def OnSize(self, event):
        """
        Handle window resize events.

        Adjusts grid column sizes proportionally based on the window width
        to ensure optimal display of information.

        :param event: The size event (optional)
        :type event: wx.SizeEvent
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        total_width = self.GetClientSize().GetWidth() - 10  # 10 is a magic number / the border width of the grid
        num_cols = self.grid.GetNumberCols()
        col_width = total_width // num_cols

        for col in range(num_cols):
            self.grid.SetColSize(col, col_width)

        self.grid.Layout()

        if event:
            event.Skip()

    def start_worker_thread(self):
        """
        Start the worker thread for generating rounds.

        Creates and starts a new RoundWorkerThread with the current configuration
        if no worker thread is currently running.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
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
        """
        Callback method called when a round is generated by the worker thread.

        Updates the UI with the new round data, including progress indicators
        and the display of the latest generated round.

        :param round_data: The generated round data
        :type round_data: list[frozenset[int]]
        :param round_number: Current round number
        :type round_number: int
        :param max_rounds: Maximum number of rounds
        :type max_rounds: int
        :param paused: Whether the worker thread is paused
        :type paused: bool
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        self.rounds.append(round_data)
        self.generated_rounds_number = round_number
        self.max_rounds_number = max_rounds
        self.round_selector_tctrl.SetMax(round_number)

        self.round_progress_text_ctrl.SetValue(f"{round_number} / {max_rounds}")
        self.update_status(paused)

    def update_status(self, paused: bool):
        """
        Update the UI status based on worker thread state.

        Updates status indicators and controls to reflect the current
        state of the worker thread (running, paused, or stopped).

        :param paused: Whether the worker thread is paused
        :type paused: bool
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
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
        """
        Render the grid with group assignments for a specific round.

        Populates the grid with group assignments from the specified round,
        displaying group labels and person names in their assigned groups.

        :param page: Round index to display (0-based)
        :type page: int
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
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
        """
        Set up the UI status before starting group generation.

        Resets status controls to their initial state and prepares the UI
        for a new round generation process.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        self.status_text_ctrl.SetValue("Setting up...")
        self.pause_button.Enable(False)
        self.round_progress_text_ctrl.SetValue("0 / 0")
        self.grid.ClearGrid()
        self.current_round = 0
        self.round_selector_tctrl.SetValue("1")

    def stop_worker_thread(self):
        """
        Stop the worker thread if it's running.

        Safely terminates the worker thread and updates the UI
        to reflect the stopped state.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        if self.worker_thread is not None:
            self.worker_thread.stop()
            self.worker_thread.join(2)
            self.worker_thread = None
            self.worker_running = False
            self.status_text_ctrl.SetValue("Stopped")
            self.pause_button.Enable(False)
            self.round_progress_text_ctrl.SetValue("0 / 0")