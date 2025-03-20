import wx
from .utility.csv_read import detect_csv_separator_and_load
from .utility.nothing import nothing
from .layout.csv_name_dia import CSVNameDialog


class NameDialog(CSVNameDialog):
    """
    Dialog for selecting name and surname columns from a CSV file.

    This dialog allows users to load a CSV file, view its contents, and select which
    columns represent names and surnames.

    :param parent: The parent window
    :type parent: wx.Window
    """
    def __init__(self, parent):
        """
        Initialize the NameDialog.

        :param parent: The parent window
        :type parent: wx.Window
        """
        super(NameDialog, self).__init__(parent)
        self.parent = parent
        self.delimiter: str | None = None
        self.encoding: str | None = None

    def on_close_window(self, event):
        """
        Handle the window close event.

        Sets the parent's csv_cancel attribute to True and closes the dialog.

        :param event: The window close event
        :type event: wx.CloseEvent
        """
        self.parent.csv_cancel = True
        self.EndModal(wx.ID_CANCEL)
        event.Skip()

    def on_header_check(self, event):
        """
        Handle the header checkbox event.

        Updates the parent's csv_has_header attribute based on the checkbox state.

        :param event: The checkbox event
        :type event: wx.CommandEvent
        """
        self.parent.csv_has_header = self.has_header_box.GetValue()
        event.Skip()

    def on_name_check(self, event):
        """
        Handle selection of name column.

        Ensures only one column can be selected as the name column and
        updates the parent's csv_name_index attribute accordingly.

        :param event: The list event
        :type event: wx.CommandEvent
        """
        checked_index = event.GetSelection()
        is_checked = self.check_name.IsChecked(checked_index)
        for i in range(self.check_name.GetCount()):
            if i != checked_index:
                self.check_name.Check(i, False)
        for i in range(self.check_sur_name.GetCount()):
            if i == checked_index:
                self.check_sur_name.Check(i, False)
        if checked_index == self.parent.csv_surname_index:
            self.parent.csv_surname_index = None
        self.parent.csv_name_index = checked_index if is_checked else None
        event.Skip()

    def on_surname_check(self, event):
        """
        Handle selection of surname column.

        Ensures only one column can be selected as the surname column and
        updates the parent's csv_surname_index attribute accordingly.

        :param event: The list event
        :type event: wx.CommandEvent
        """
        checked_index = event.GetSelection()
        is_checked = self.check_sur_name.IsChecked(checked_index)
        for i in range(self.check_sur_name.GetCount()):
            if i != checked_index:
                self.check_sur_name.Check(i, False)
        for i in range(self.check_name.GetCount()):
            if i == checked_index:
                self.check_name.Check(i, False)
        if checked_index == self.parent.csv_name_index:
            self.parent.csv_name_index = None
        self.parent.csv_surname_index = checked_index if is_checked else None
        event.Skip()

    def on_nothing(self, event):
        """
        Handle event that does nothing.

        Calls the nothing function from the utility module.

        :param event: The event
        :type event: wx.Event
        """
        nothing()
        event.Skip()

    def on_done_click(self, event):
        """
        Handle the done button click event.

        Closes the dialog with an OK status.

        :param event: The button event
        :type event: wx.CommandEvent
        """
        # self.parent.csv_name_index = self.check_name.GetSelection()
        # self.parent.csv_surname_index = self.check_sur_name.GetSelection()
        self.EndModal(wx.ID_OK)
        event.Skip()

    def on_load(self, event):
        """
        Handle the load button click event.

        Loads the CSV file, displays its contents in the grid, and populates
        the column selection checkboxes.

        :param event: The button event
        :type event: wx.CommandEvent
        """
        data, delimiter, encoding = detect_csv_separator_and_load(self.parent.csv_path)
        self.parent.csv_data = data
        self.delimiter = delimiter
        self.encoding = encoding

        self.csv_display_grid.ClearGrid()

        # Adjust the grid size
        self.csv_display_grid.DeleteCols(0, self.csv_display_grid.GetNumberCols())
        self.csv_display_grid.DeleteRows(0, self.csv_display_grid.GetNumberRows())
        self.csv_display_grid.AppendCols(len(data[0]))
        self.csv_display_grid.AppendRows(len(data))

        # Assign the data to the grid
        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                self.csv_display_grid.SetCellValue(row_idx, col_idx, value)

        self.csv_display_grid.AutoSizeColumns()
        self.csv_display_grid.AutoSizeRows()
        self.csv_display_grid.ForceRefresh()

        self.parent.csv_has_header = self.has_header_box.GetValue()

        self.check_name.Set(data[0])
        self.check_name.Fit()
        self.check_sur_name.Set(data[0])
        self.check_sur_name.Fit()

        self.Fit()
        event.Skip()