import wx
from groupbuilder.csv_name_picker_dialog import NameDialog
from groupbuilder.file_picker_dialog import FilePickDialog

class MyFrame(wx.Frame):
    def __init__(self, parent):
        super(MyFrame, self).__init__(parent, -1, "Group Builder", size=(800, 600))
        self.csv_path: str | None = None
        self.csv_data: list[list] | None = None
        self.csv_has_header: bool | None = None
        self.csv_name_index: int | None = None
        self.csv_surname_index: int | None = None

        self.csv_name_dialog = NameDialog(self)
        self.csv_pick_dialog = FilePickDialog(self)

        self.Bind(wx.EVT_MOVE, self.on_open, self)

    def on_open(self, event):
        while not self.csv_path:
            self.csv_pick_dialog.ShowModal()
        self.csv_pick_dialog.Destroy()
        self.csv_name_dialog.ShowModal()
        self.csv_name_dialog.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
