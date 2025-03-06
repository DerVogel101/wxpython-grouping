import wx
from .layout.csv_filepick_dia import CSVPickDialog

class FilePickDialog(CSVPickDialog):
    def __init__(self, parent):
        super(FilePickDialog, self).__init__(parent)
        self.parent = parent

    def on_done( self, event ):
        self.parent.csv_path = self.csv_pick.GetPath()
        self.EndModal(wx.ID_OK)
        event.Skip()
