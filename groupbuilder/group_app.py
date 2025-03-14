import wx
from .layout.layout_base import AppFrame
from .csv_name_picker_dialog import NameDialog
from .file_picker_dialog import FilePickDialog

class GroupApp(AppFrame):
    def __init__(self, parent):
        super(GroupApp, self).__init__(parent)
        self.csv_pick_dialog: NameDialog | None = None
        self.csv_name_dialog: FilePickDialog | None = None
        self.csv_path: str | None = None
        self.csv_data: list[list] | None = None
        self.csv_has_header: bool | None = None
        self.csv_name_index: int | None = None
        self.csv_surname_index: int | None = None
        self.csv_cancel: bool = False

    def on_round_left_click( self, event ):
        event.Skip()

    def on_round_selector_enter( self, event ):
        event.Skip()

    def on_round_right_click( self, event ):
        event.Skip()

    def on_csv_load_button_click( self, event ):
        self.csv_path = None
        self.csv_data = None
        self.csv_has_header = None
        self.csv_name_index = None
        self.csv_surname_index = None

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

        event.Skip()

    def on_gconfig_button_click( self, event ):
        event.Skip()

    def on_pause_button_click( self, event ):
        event.Skip()

    def on_csv_export_change( self, event ):
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = GroupApp(None)
    frame.Show()
    app.MainLoop()
