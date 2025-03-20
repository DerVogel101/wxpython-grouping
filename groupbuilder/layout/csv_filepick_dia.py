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
## Class CSVPickDialog
###########################################################################

class CSVPickDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Datei auswählen"), pos = wx.DefaultPosition, size = wx.Size( 449,129 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"CSV Datei Auswählen:"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText3.Wrap( -1 )

        bSizer5.Add( self.m_staticText3, 1, wx.ALIGN_CENTER|wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.TOP, 15 )

        self.csv_pick = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.csv"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_USE_TEXTCTRL )
        bSizer5.Add( self.csv_pick, 2, wx.ALIGN_BOTTOM|wx.BOTTOM|wx.RIGHT|wx.TOP, 15 )


        bSizer9.Add( bSizer5, 0, wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.pick_done = wx.Button( self, wx.ID_ANY, _(u"Fertig"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.pick_done, 1, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, 15 )


        bSizer9.Add( bSizer8, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_close_window )
        self.pick_done.Bind( wx.EVT_BUTTON, self.on_done )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_close_window( self, event ):
        event.Skip()

    def on_done( self, event ):
        event.Skip()


