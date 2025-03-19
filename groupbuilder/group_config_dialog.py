import wx

from .layout.group_conf_dia import GroupConfigurationDialog
from .core.algorithm import GroupingAlgorithm
from .core.sys_utils import SysUtils

class GroupConfigDialog(GroupConfigurationDialog):
    def __init__(self, parent, person_size: int | None = None, size_locked: bool = False):
        super(GroupConfigDialog, self).__init__(parent)
        self.parent = parent
        self.group_size: int | None = None
        self.person_size: int | None = person_size
        self.needed_ram: int | None = None
        self.available_ram: int | None = None
        self.locked: bool = size_locked

    def on_init( self, event ):
        if self.locked:
            self.person_comb.Enable(False)
            self.person_comb.SetValue(str(self.person_size))
        self.group_size = int(self.group_comb.GetValue())
        self.person_size = int(self.person_comb.GetValue())
        self.display_ram_usage()
        event.Skip()

    def on_person_select( self, event ):
        self.person_handler(event)

    def on_person_enter( self, event ):
        self.person_handler(event)

    def on_group_select( self, event ):
        self.group_handler(event)

    def on_group_enter( self, event ):
        self.group_handler(event)

    def on_config_cancel_click( self, event ):
        self.parent.group_config_cancel = True
        self.EndModal(wx.ID_CANCEL)
        event.Skip()

    def on_config_done_click( self, event ):
        if self.needed_ram > self.available_ram:
            dialog = wx.MessageDialog(parent=self,
                                      message=f"Die benötigte RAM-Größe ({self.needed_ram} MB) ist größer als die verfügbare RAM-Größe ({self.available_ram} MB).\n"
                                              f"Dies könnte zu Performance- oder Stabilitätsproblemen führen.\n"
                                              f"Möchten Sie trotzdem fortfahren?",
                                      caption="RAM-Größe",
                                      style=wx.YES_NO | wx.ICON_WARNING)
            result = dialog.ShowModal()
            if result == wx.ID_NO:
                event.Skip()
                return
        self.parent.group_size = self.group_size
        self.parent.person_size = self.person_size
        self.EndModal(wx.ID_OK)
        event.Skip()

    def person_handler(self, event):
        # if self.locked:
        #     self.person_comb.SetValue(str(self.person_size))
        #     wx.MessageBox("Die Anzahl der Personen kann nicht geändert werden, wenn die Personenmenge festgelegt ist.",
        #                   "Gruppengröße festgelegt", wx.OK | wx.ICON_ERROR)
        #     event.Skip()
        try:
            person_size = int(self.person_comb.GetValue())
            if self.group_size:
                if person_size > self.group_size:
                    self.person_size = person_size
                else:
                    raise ValueError("Personenanzahl muss größer als Gruppengröße sein.")
            self.display_ram_usage()
        except ValueError as e:
            self.person_comb.SetValue(str(self.person_size))
            wx.MessageBox(f"Bitte gebe eine valide Zahl an.\n{e}", "Invalide Eingabe", wx.OK | wx.ICON_ERROR)
        event.Skip()

    def group_handler(self, event):
        try:
            group_size = int(self.group_comb.GetValue())
            if self.person_size:
                if group_size < self.person_size:
                    self.group_size = group_size
                else:
                    raise ValueError("Gruppengröße muss kleiner als Personenanzahl sein.")
            self.display_ram_usage()
        except ValueError as e:
            self.group_comb.SetValue(str(self.group_size))
            wx.MessageBox(f"Bitte gebe eine valide Zahl an.\n{e}", "Invalide Eingabe", wx.OK | wx.ICON_ERROR)
        event.Skip()

    def display_ram_usage(self):
        needed_ram = int(GroupingAlgorithm.get_ops_needed(self.person_size, self.group_size)[2]) # MB
        available_ram = SysUtils.get_available_memory()
        self.ram_usage_gauge.SetValue(0)
        self.ram_usage_gauge.SetRange(available_ram)
        # FIXME: Colour is not changing under Windows
        self.ram_usage_gauge.SetBackgroundColour(wx.GREEN)
        self.ram_usage_text.SetForegroundColour(wx.BLACK)

        if needed_ram > available_ram:
            self.ram_usage_gauge.SetValue(available_ram)
        else:
            self.ram_usage_gauge.SetValue(needed_ram)
        if (needed_ram / available_ram) > 0.8:
            self.ram_usage_gauge.SetBackgroundColour(wx.RED)
            # FIXME: Colour is not changing under Windows

        self.ram_usage_text.SetLabel(f"{needed_ram} / {available_ram} MB")

        self.Layout()

        if needed_ram / available_ram > 0.85:
            self.ram_usage_text.SetForegroundColour(wx.RED)
            self.RequestUserAttention()

        self.available_ram = available_ram
        self.needed_ram = needed_ram