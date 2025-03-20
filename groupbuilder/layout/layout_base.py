# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class AppFrame
###########################################################################

class AppFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Gruppenerzeuger | Einzigartig"), pos = wx.DefaultPosition, size = wx.Size( 853,507 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 853,507 ), wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        fgSizer1 = wx.FlexGridSizer( 5, 0, 5, 0 )
        fgSizer1.AddGrowableCol( 0 )
        fgSizer1.AddGrowableRow( 4 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        fgSizer1.Add( self.m_staticline6, 0, 0, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer9.SetMinSize( wx.Size( -1,33 ) )
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Generierte Runden:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        self.m_staticText9.SetMinSize( wx.Size( 115,-1 ) )

        bSizer9.Add( self.m_staticText9, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.round_progress_text_ctrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_NO_VSCROLL|wx.TE_READONLY )
        bSizer9.Add( self.round_progress_text_ctrl, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.round_selector_tctrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 1, 1, 1 )
        bSizer9.Add( self.round_selector_tctrl, 3, wx.ALL, 5 )


        bSizer9.Add( ( 0, 0), 6, wx.EXPAND, 5 )

        self.csv_load_button = wx.Button( self, wx.ID_ANY, _(u"CSV Datei laden"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.csv_load_button.SetMinSize( wx.Size( 125,-1 ) )

        bSizer9.Add( self.csv_load_button, 1, wx.ALL, 5 )

        self.group_config_button = wx.Button( self, wx.ID_ANY, _(u"Konfigurieren"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.group_config_button.SetMinSize( wx.Size( 125,-1 ) )

        bSizer9.Add( self.group_config_button, 1, wx.ALL, 5 )


        fgSizer1.Add( bSizer9, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer3.SetMinSize( wx.Size( -1,33 ) )
        self.m_static_text7 = wx.StaticText( self, wx.ID_ANY, _(u"Generierungs Status:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_static_text7.Wrap( -1 )

        self.m_static_text7.SetMinSize( wx.Size( 115,-1 ) )

        bSizer3.Add( self.m_static_text7, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.status_text_ctrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_NO_VSCROLL|wx.TE_READONLY )
        bSizer3.Add( self.status_text_ctrl, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.pause_button = wx.Button( self, wx.ID_ANY, _(u"Pause / Weiter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.pause_button, 1, wx.ALL, 5 )


        bSizer3.Add( ( 0, 0), 6, wx.EXPAND, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"Runden Export zu CSV:"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.m_staticText11.Wrap( -1 )

        self.m_staticText11.SetMinSize( wx.Size( 125,-1 ) )

        bSizer3.Add( self.m_staticText11, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.export_file_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Datei Exportieren"), _(u"*.csv"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE )
        self.export_file_picker.SetMinSize( wx.Size( 125,-1 ) )

        bSizer3.Add( self.export_file_picker, 1, wx.ALL, 5 )


        fgSizer1.Add( bSizer3, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )

        self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        fgSizer1.Add( self.m_staticline5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

        self.grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.grid.CreateGrid( 2, 2 )
        self.grid.EnableEditing( False )
        self.grid.EnableGridLines( True )
        self.grid.EnableDragGridSize( False )
        self.grid.SetMargins( 0, 0 )

        # Columns
        self.grid.EnableDragColMove( False )
        self.grid.EnableDragColSize( False )
        self.grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.grid.EnableDragRowSize( False )
        self.grid.SetRowLabelSize( 0 )
        self.grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.grid.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
        fgSizer1.Add( self.grid, 10, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( fgSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_close )
        self.round_selector_tctrl.Bind( wx.EVT_SPINCTRL, self.on_round_selector_enter )
        self.round_selector_tctrl.Bind( wx.EVT_TEXT_ENTER, self.on_round_selector_enter )
        self.csv_load_button.Bind( wx.EVT_BUTTON, self.on_csv_load_button_click )
        self.group_config_button.Bind( wx.EVT_BUTTON, self.on_gconfig_button_click )
        self.pause_button.Bind( wx.EVT_BUTTON, self.on_pause_button_click )
        self.export_file_picker.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_csv_export_change )
        self.grid.Bind( wx.EVT_SIZE, self.OnSize )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_close( self, event ):
        event.Skip()

    def on_round_selector_enter( self, event ):
        event.Skip()


    def on_csv_load_button_click( self, event ):
        event.Skip()

    def on_gconfig_button_click( self, event ):
        event.Skip()

    def on_pause_button_click( self, event ):
        event.Skip()

    def on_csv_export_change( self, event ):
        event.Skip()

    def OnSize( self, event ):
        event.Skip()


