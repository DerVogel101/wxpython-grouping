# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class GroupConfigurationDialog
###########################################################################

class GroupConfigurationDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Gruppenkonfiguration"), pos = wx.DefaultPosition, size = wx.Size( 467,189 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.Size( 381,165 ), wx.Size( -1,-1 ) )

        fgSizer3 = wx.FlexGridSizer( 4, 0, 0, 0 )
        fgSizer3.AddGrowableCol( 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Personenanzahl:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer1.Add( self.m_staticText1, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        person_combChoices = [ _(u"8"), _(u"10"), _(u"13"), _(u"15"), _(u"20") ]
        self.person_comb = wx.ComboBox( self, wx.ID_ANY, _(u"8"), wx.DefaultPosition, wx.DefaultSize, person_combChoices, wx.TE_PROCESS_ENTER )
        bSizer1.Add( self.person_comb, 3, wx.ALL, 5 )


        fgSizer3.Add( bSizer1, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Gruppengröße:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer2.Add( self.m_staticText2, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        group_combChoices = [ _(u"2"), _(u"3"), _(u"4"), _(u"5"), _(u"6") ]
        self.group_comb = wx.ComboBox( self, wx.ID_ANY, _(u"2"), wx.DefaultPosition, wx.DefaultSize, group_combChoices, wx.TE_PROCESS_ENTER )
        bSizer2.Add( self.group_comb, 3, wx.ALL, 5 )


        fgSizer3.Add( bSizer2, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Speicherbedarf:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer8.Add( self.m_staticText6, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.ram_usage_text = wx.TextCtrl( self, wx.ID_ANY, _(u"? / ? MB"), wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer8.Add( self.ram_usage_text, 3, wx.ALL|wx.EXPAND, 5 )


        fgSizer3.Add( bSizer8, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer10.SetMinSize( wx.Size( -1,40 ) )
        self.groupconf_cancel_button = wx.Button( self, wx.ID_ANY, _(u"Abbrechen"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.groupconf_cancel_button, 1, wx.ALIGN_CENTER, 5 )

        self.groupconf_done_button = wx.Button( self, wx.ID_ANY, _(u"Fertig"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.groupconf_done_button, 1, wx.ALIGN_CENTER, 5 )


        fgSizer3.Add( bSizer10, 1, wx.ALIGN_RIGHT|wx.ALIGN_TOP|wx.BOTTOM|wx.RIGHT, 10 )


        self.SetSizer( fgSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_config_cancel_click )
        self.Bind( wx.EVT_INIT_DIALOG, self.on_init )
        self.person_comb.Bind( wx.EVT_COMBOBOX, self.on_person_select )
        self.person_comb.Bind( wx.EVT_TEXT_ENTER, self.on_person_enter )
        self.group_comb.Bind( wx.EVT_COMBOBOX, self.on_group_select )
        self.group_comb.Bind( wx.EVT_TEXT_ENTER, self.on_group_enter )
        self.groupconf_cancel_button.Bind( wx.EVT_BUTTON, self.on_config_cancel_click )
        self.groupconf_done_button.Bind( wx.EVT_BUTTON, self.on_config_done_click )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_config_cancel_click( self, event ):
        event.Skip()

    def on_init( self, event ):
        event.Skip()

    def on_person_select( self, event ):
        event.Skip()

    def on_person_enter( self, event ):
        event.Skip()

    def on_group_select( self, event ):
        event.Skip()

    def on_group_enter( self, event ):
        event.Skip()


    def on_config_done_click( self, event ):
        event.Skip()


