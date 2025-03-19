import csv
from wx.grid import Grid

def export_grid_to_csv(grid: Grid, filename: str) -> None:
        """
        Export the contents of a wx.Grid to a CSV file.

        Args:
            grid (Grid): The wx.Grid instance containing the data to export.
            filename (str): The name of the CSV file to write the data to.

        Returns:
            None
        """
        rows = grid.GetNumberRows()
        cols = grid.GetNumberCols()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for row in range(rows):
                row_data = []
                for col in range(cols):
                    row_data.append(grid.GetCellValue(row, col))
                writer.writerow(row_data)