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
## Class CSVNameDialog
###########################################################################

class CSVNameDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Select Name Columns"), pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.Size( 1080,720 ) )

        fgSizer2 = wx.FlexGridSizer( 3, 3, 0, 0 )
        fgSizer2.AddGrowableCol( 0 )
        fgSizer2.AddGrowableRow( 1 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Vorname"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        fgSizer2.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"Nachname"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        fgSizer2.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.csv_display_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.csv_display_grid.CreateGrid( 5, 5 )
        self.csv_display_grid.EnableEditing( False )
        self.csv_display_grid.EnableGridLines( True )
        self.csv_display_grid.EnableDragGridSize( False )
        self.csv_display_grid.SetMargins( 0, 0 )

        # Columns
        self.csv_display_grid.SetColSize( 0, 80 )
        self.csv_display_grid.SetColSize( 1, 80 )
        self.csv_display_grid.SetColSize( 2, 79 )
        self.csv_display_grid.SetColSize( 3, 80 )
        self.csv_display_grid.SetColSize( 4, 80 )
        self.csv_display_grid.EnableDragColMove( False )
        self.csv_display_grid.EnableDragColSize( True )
        self.csv_display_grid.SetColLabelSize( 0 )
        self.csv_display_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.csv_display_grid.AutoSizeRows()
        self.csv_display_grid.EnableDragRowSize( True )
        self.csv_display_grid.SetRowLabelSize( 0 )
        self.csv_display_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.csv_display_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.csv_display_grid.SetMinSize( wx.Size( 500,200 ) )
        self.csv_display_grid.SetMaxSize( wx.Size( 600,300 ) )

        fgSizer2.Add( self.csv_display_grid, 0, wx.ALL, 5 )

        check_nameChoices = []
        self.check_name = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, check_nameChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.LB_SINGLE )
        fgSizer2.Add( self.check_name, 0, wx.ALL|wx.EXPAND, 5 )

        check_sur_nameChoices = []
        self.check_sur_name = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, check_sur_nameChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.LB_SINGLE )
        fgSizer2.Add( self.check_sur_name, 0, wx.ALL|wx.EXPAND, 5 )

        self.has_header_box = wx.CheckBox( self, wx.ID_ANY, _(u"Erste Zeile ist ein Header"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.has_header_box.SetValue(True)
        fgSizer2.Add( self.has_header_box, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, _(u"Nutzlos"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.name_select_done = wx.Button( self, wx.ID_ANY, _(u"Fertig"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.name_select_done, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        self.SetSizer( fgSizer2 )
        self.Layout()
        fgSizer2.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_close_window )
        self.Bind( wx.EVT_INIT_DIALOG, self.on_load )
        self.check_name.Bind( wx.EVT_CHECKLISTBOX, self.on_name_check )
        self.check_sur_name.Bind( wx.EVT_CHECKLISTBOX, self.on_surname_check )
        self.has_header_box.Bind( wx.EVT_CHECKBOX, self.on_header_check )
        self.m_button3.Bind( wx.EVT_BUTTON, self.on_nothing )
        self.name_select_done.Bind( wx.EVT_BUTTON, self.on_done_click )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_close_window( self, event ):
        event.Skip()

    def on_load( self, event ):
        event.Skip()

    def on_name_check( self, event ):
        event.Skip()

    def on_surname_check( self, event ):
        event.Skip()

    def on_header_check( self, event ):
        event.Skip()

    def on_nothing( self, event ):
        event.Skip()

    def on_done_click( self, event ):
        event.Skip()


