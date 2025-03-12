import wx
from .layout.csv_filepick_dia import CSVPickDialog

class FilePickDialog(CSVPickDialog):
    def __init__(self, parent):
        super(FilePickDialog, self).__init__(parent)
        self.parent = parent

    def on_done( self, event ):
        if self.csv_pick.GetPath():
            self.parent.csv_path = self.csv_pick.GetPath()
            self.EndModal(wx.ID_OK)
        event.Skip()

    def on_close_window( self, event ):
        self.parent.csv_cancel = True
        self.EndModal(wx.ID_CANCEL)
        event.Skip()
