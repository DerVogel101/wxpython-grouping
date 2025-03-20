import wx
from groupbuilder.group_app import GroupApp

def main():
    """
    Main entry point for the Group Builder application.

    This function initializes the wxPython application, creates the main
    application frame, displays it, and starts the main event loop.

    The application will continue running until the main window is closed
    or the application is otherwise terminated.
    """
    app = wx.App()
    frame = GroupApp(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
