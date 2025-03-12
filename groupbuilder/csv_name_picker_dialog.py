import wx
from .utility.csv_read import detect_csv_separator_and_load
from .utility.nothing import nothing
from .layout.csv_name_dia import CSVNameDialog


class NameDialog(CSVNameDialog):
    def __init__(self, parent):
        super(NameDialog, self).__init__(parent)
        self.parent = parent
        self.delimiter: str | None = None
        self.encoding: str | None = None

    def on_close_window( self, event ):
        self.parent.csv_cancel = True
        self.EndModal(wx.ID_CANCEL)
        event.Skip()

    def on_header_check( self, event ):
        self.parent.csv_has_header = self.has_header_box.GetValue()
        event.Skip()

    def on_name_check( self, event ):
        checked_index = event.GetSelection()
        for i in range(self.check_name.GetCount()):
            if i != checked_index:
                self.check_name.Check(i, False)
        for i in range(self.check_sur_name.GetCount()):
            if i == checked_index:
                self.check_sur_name.Check(i, False)
        event.Skip()

    def on_surname_check( self, event ):
        checked_index = event.GetSelection()
        for i in range(self.check_sur_name.GetCount()):
            if i != checked_index:
                self.check_sur_name.Check(i, False)
        for i in range(self.check_name.GetCount()):
            if i == checked_index:
                self.check_name.Check(i, False)
        event.Skip()

    def on_nothing( self, event ):
        nothing()
        event.Skip()

    def on_done_click( self, event ):
        self.parent.csv_name_index = self.check_name.GetSelection()
        self.parent.csv_surname_index = self.check_sur_name.GetSelection()
        self.EndModal(wx.ID_OK)
        event.Skip()

    def on_load( self, event ):
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