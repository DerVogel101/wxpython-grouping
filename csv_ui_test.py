import wx
from groupbuilder.group_app import GroupApp

if __name__ == '__main__':
    app = wx.App()
    frame = GroupApp(None)
    frame.Show()
    app.MainLoop()
