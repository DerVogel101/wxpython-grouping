"""
File Picker Dialog Module
========================

This module provides a dialog interface for selecting CSV files to be used in the application.

.. inheritance-diagram:: groupbuilder.file_picker_dialog
   :parts: 1

.. autosummary::
   :toctree: generated/

   FilePickDialog
"""

import wx
from .layout.csv_filepick_dia import CSVPickDialog

class FilePickDialog(CSVPickDialog):
    """
    A dialog for picking a CSV file.

    This dialog allows users to browse and select a CSV file from their filesystem.

    .. inheritance-diagram:: groupbuilder.file_picker_dialog.FilePickDialog
       :parts: 1

    .. autosummary::
       :toctree: generated/

       __init__
       on_done
       on_close_window
    """
    def __init__(self, parent):
        """
        Initialize the FilePickDialog.

        :param parent: The parent window
        :type parent: wx.Window
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        super(FilePickDialog, self).__init__(parent)
        self.parent = parent

    def on_done(self, event):
        """
        Handle the done button click event.

        If a CSV file is selected, set the parent's csv_path attribute and close the dialog with an OK status.

        :param event: The event object
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        if self.csv_pick.GetPath():
            self.parent.csv_path = self.csv_pick.GetPath()
            self.EndModal(wx.ID_OK)
        event.Skip()

    def on_close_window(self, event):
        """
        Handle the window close event.

        Set the parent's csv_cancel attribute to True and close the dialog with a CANCEL status.

        :param event: The event object
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        self.parent.csv_cancel = True
        self.EndModal(wx.ID_CANCEL)
        event.Skip()