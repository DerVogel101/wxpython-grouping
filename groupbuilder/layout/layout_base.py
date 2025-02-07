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
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 736,507 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        fgSizer1 = wx.FlexGridSizer( 4, 0, 5, 0 )
        self.fgSizer1 = fgSizer1
        fgSizer1.AddGrowableCol( 0 )
        fgSizer1.AddGrowableRow( 2 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer1.Add( self.m_staticText1, 7, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        combo_box_1Choices = [ _(u"1"), _(u"2"), _(u"3"), _(u"4") ]
        self.combo_box_1 = wx.ComboBox( self, wx.ID_ANY, _(u"1"), wx.DefaultPosition, wx.DefaultSize, combo_box_1Choices, 0 )
        bSizer1.Add( self.combo_box_1, 1, wx.ALL, 5 )


        fgSizer1.Add( bSizer1, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer2.Add( self.m_staticText2, 7, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        combo_box_2Choices = [ _(u"1"), _(u"2"), _(u"3"), _(u"4") ]
        self.combo_box_2 = wx.ComboBox( self, wx.ID_ANY, _(u"1"), wx.DefaultPosition, wx.DefaultSize, combo_box_2Choices, 0 )
        bSizer2.Add( self.combo_box_2, 1, wx.ALL, 5 )


        fgSizer1.Add( bSizer2, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )

        self.grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.grid.CreateGrid( 2, 2 )
        self.grid.EnableEditing( True )
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
        self.grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
        fgSizer1.Add( self.grid, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer3.SetMinSize( wx.Size( -1,33 ) )

        bSizer3.Add( ( 0, 0), 5, wx.EXPAND, 5 )

        self.add_button = wx.Button( self, wx.ID_ANY, _(u"Hinzufügen"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.add_button, 1, wx.ALL, 5 )

        self.remove_button = wx.Button( self, wx.ID_ANY, _(u"Entfernen"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.remove_button, 1, wx.ALL, 5 )


        fgSizer1.Add( bSizer3, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )


        self.SetSizer( fgSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.grid.Bind( wx.EVT_SIZE, self.OnSize )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnSize( self, event ):
        event.Skip()


