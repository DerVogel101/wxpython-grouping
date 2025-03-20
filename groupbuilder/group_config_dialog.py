"""
Group Configuration Dialog Module
===============================

This module provides a dialog interface for configuring group settings, including
group size and number of persons, with RAM usage estimation.

.. inheritance-diagram:: groupbuilder.group_config_dialog
   :parts: 1

.. autosummary::
   :toctree: generated/

   GroupConfigDialog
"""

import wx

from .layout.group_conf_dia import GroupConfigurationDialog
from .core.algorithm import GroupingAlgorithm
from .core.sys_utils import SysUtils

class GroupConfigDialog(GroupConfigurationDialog):
    """
    A dialog for configuring group settings.

    This dialog allows users to specify the number of persons and group size,
    provides RAM usage estimation, and warns about potential memory issues.

    .. inheritance-diagram:: groupbuilder.group_config_dialog.GroupConfigDialog
       :parts: 1

    .. autosummary::
       :toctree: generated/

       __init__
       on_init
       on_person_select
       on_person_enter
       on_group_select
       on_group_enter
       on_config_cancel_click
       on_config_done_click
       person_handler
       group_handler
       display_ram_usage
    """
    def __init__(self, parent, person_size: int | None = None, size_locked: bool = False):
        """
        Initialize the GroupConfigDialog.

        :param parent: The parent window
        :type parent: wx.Window
        :param person_size: The initial number of persons, defaults to None
        :type person_size: int | None, optional
        :param size_locked: Whether the person size is locked, defaults to False
        :type size_locked: bool, optional
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        super(GroupConfigDialog, self).__init__(parent)
        self.parent = parent
        self.group_size: int | None = None
        self.person_size: int | None = person_size
        self.needed_ram: int | None = None
        self.available_ram: int | None = None
        self.locked: bool = size_locked

    def on_init(self, event):
        """
        Initialize the dialog.

        Sets initial values for the dialog controls based on current configuration
        and displays estimated RAM usage.

        :param event: The initialization event
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        if self.locked:
            self.person_comb.Enable(False)
            self.person_comb.SetValue(str(self.person_size))
        self.group_size = int(self.group_comb.GetValue())
        self.person_size = int(self.person_comb.GetValue())
        self.display_ram_usage()
        event.Skip()

    def on_person_select(self, event):
        """
        Handle person selection event.

        Delegates to the person_handler method when a person count is selected.

        :param event: The selection event
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        self.person_handler(event)

    def on_person_enter(self, event):
        """
        Handle person enter event.

        Delegates to the person_handler method when a person count is entered.

        :param event: The text enter event
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        self.person_handler(event)

    def on_group_select(self, event):
        """
        Handle group selection event.

        Delegates to the group_handler method when a group size is selected.

        :param event: The selection event
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        self.group_handler(event)

    def on_group_enter(self, event):
        """
        Handle group enter event.

        Delegates to the group_handler method when a group size is entered.

        :param event: The text enter event
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        self.group_handler(event)

    def on_config_cancel_click(self, event):
        """
        Handle cancel button click event.

        Sets the parent's group_config_cancel flag to True and closes the dialog.

        :param event: The button click event
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        self.parent.group_config_cancel = True
        self.EndModal(wx.ID_CANCEL)
        event.Skip()

    def on_config_done_click(self, event):
        """
        Handle done button click event.

        Warns the user if RAM usage might be excessive, and if they continue,
        updates the parent's configuration and closes the dialog with OK status.

        :param event: The button click event
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
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
        """
        Handle person input events.

        Validates user input for person count, ensuring it's a valid number and
        consistent with the selected group size.

        :param event: The input event
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        try:
            person_size = int(self.person_comb.GetValue())
            if person_size > 691337:
                wx.MessageBox("Träum weiter.", "Zu viele Personen", wx.OK | wx.ICON_ERROR)
                self.person_comb.SetValue(str(self.person_size))
                event.Skip()
                return
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
        """
        Handle group input events.

        Validates user input for group size, ensuring it's a valid number and
        consistent with the selected person count.

        :param event: The input event
        :type event: wx.Event
        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        try:
            group_size = int(self.group_comb.GetValue())
            if group_size > 691337:
                wx.MessageBox("Träum weiter.", "Zu viele Gruppen", wx.OK | wx.ICON_ERROR)
                self.group_comb.SetValue(str(self.group_size))
                event.Skip()
                return
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
        """
        Display the RAM usage based on the current group and person sizes.

        Calculates and displays the estimated RAM usage for the configured group and
        person sizes, highlighting excessive usage in red.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        needed_ram = int(GroupingAlgorithm.get_ops_needed(self.person_size, self.group_size)[2]) # MB
        available_ram = SysUtils.get_available_memory()

        self.ram_usage_text.SetLabel(f"{needed_ram} / {available_ram} MB")

        self.Layout()

        if needed_ram / available_ram > 0.85:
            self.ram_usage_text.SetForegroundColour(wx.RED)
            self.RequestUserAttention()
        else:
            self.ram_usage_text.SetForegroundColour(wx.BLACK)

        self.available_ram = available_ram
        self.needed_ram = needed_ram