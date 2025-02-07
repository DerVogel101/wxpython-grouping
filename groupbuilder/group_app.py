from layout_base import MyFrame
import wx


class MyAPPFrame(MyFrame):
    def __init__(self):
        super().__init__(None)
        self.SetTitle("MyAPP")
        self.SetColumnWidths([-1, -1])
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def SetColumnWidths(self, widths):
        total_width = self.grid.GetClientSize().GetWidth()
        fixed_width = 0
        proportional_count = 0

        for width in widths:
            if width > 0:
                fixed_width += width
            else:
                proportional_count += -width

        for i, width in enumerate(widths):
            if width > 0:
                self.grid.SetColSize(i, width)
            else:
                proportion_width = (total_width - fixed_width) * (-width) / proportional_count
                self.grid.SetColSize(i, int(proportion_width))
        self.grid.ForceRefresh()

    def SetRowHeigths(self, heigths):
        flex_height = self.fgSizer1.GetSize().GetHeight()
        print(flex_height)
        total_height = self.grid.GetClientSize().GetHeight()
        label_height = self.grid.GetColLabelSize()
        print(label_height, total_height)
        usable_height = total_height - label_height
        fixed_height = 0
        proportional_count = 0

        for height in heigths:
            if height > 0:
                fixed_height += height
            else:
                proportional_count += -height

        for i, height in enumerate(heigths):
            if height > 0:
                if height < 1:
                    pass
                else:
                    self.grid.SetRowSize(i, height)
            else:
                proportion_height = (usable_height - fixed_height) * (-height) / proportional_count
                if proportion_height < 1:
                    pass
                else:
                    self.grid.SetRowSize(i, int(proportion_height))
        self.grid.ForceRefresh()

    def OnSize( self, event ):
        self.SetColumnWidths([-1, -1])
        row_number = self.grid.GetNumberRows()
        heigths = [-1 for _ in range(row_number)]
        print(heigths)
        self.SetRowHeigths(heigths)
        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyAPPFrame()
    frame.Show()
    app.MainLoop()