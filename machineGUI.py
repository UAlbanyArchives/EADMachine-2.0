# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import sys
from datetime import date
from resource_path import resource_path

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "EADMachine 2.0", pos = wx.DefaultPosition, size = wx.Size( 1200,850 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		panel = wx.Panel(self)
		
		favicon = wx.Icon(resource_path('resources/em.gif'), wx.BITMAP_TYPE_GIF, 16, 16)
		self.SetIcon(favicon)
		
		#default information:
		processor = "unprocessed"
		publishYear = str(date.today().year)
		todayMonth = str(date.today().month)
		todayDay = str(date.today().day)
		if len(todayMonth) == 1:
			todayMonth = "0" + todayMonth
		if len(todayDay) == 1:
			todayDay = "0" + todayDay
		faCreationDate = str(date.today().year) + "-" + todayMonth + "-" + todayDay
		histNoteLabel = "Historical Note"
		acqInfo = "All items in this collection were transferred to the University Libraries, M.E. Grenander Department of Special Collections and Archives."
		arrangeStmt = "The collection is unprocessed and is likely disorganized. Individual items may be difficult to find."
		accessStmt = "<p>Access to this collection is restricted because it is unprocessed. Portions of the collection may contain recent administrative records and/or personally identifiable information. Please contact an archivist for more information.</p><p>Red asterisks (***) denote restricted items.</p>"
		useStmt = "<p>This page may contain links to digital objects. Access to these images and the technical capacity to download them does not imply permission for re-use. Digital objects may be used freely for personal reference use, referred to, or linked to from other web sites.</p><p>Researchers do not have permission to publish or disseminate material from these collections without permission from an archivist and/or the copyright holder.</p><p>The researcher assumes full responsibility for conforming to the laws of copyright. Some materials in these collections may be protected by the U.S. Copyright Law (Title 17, U.S.C.) and/or by the copyright or neighboring-rights laws of other nations. More information about U.S. Copyright is provided by the Copyright Office. Additionally, re-use may be restricted by terms of University Libraries gift or purchase agreements, donor restrictions, privacy and publicity rights, licensing and trademarks.</p><p>The University Archives are eager to hear from any copyright owners who are not properly identified so that appropriate information may be provided in the future.</p>"
		
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.saveAs = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save As EAD", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.saveAs )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.page2 = wx.Notebook( panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.page1 = wx.Panel( self.page2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.page1, wx.ID_ANY, u"Collection:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.collectionName = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.collectionName, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.page1, wx.ID_ANY, u"Collection ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self.page1, wx.ID_ANY, u"nam_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.collectionID = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 211,-1 ), 0 )
		bSizer3.Add( self.collectionID, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self.page1, wx.ID_ANY, u"Sponsor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.sponsor = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.sponsor, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.page1, wx.ID_ANY, u"Normal Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.collectionDate = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.collectionDate, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.page1, wx.ID_ANY, u"Processed by:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.processedBy = wx.TextCtrl( self.page1, wx.ID_ANY, processor, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.processedBy, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self.page1, wx.ID_ANY, u"Processing Date Normal:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.processingDate = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.processingDate, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self.page1, wx.ID_ANY, u"Publish Year:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.publishedYear = wx.TextCtrl( self.page1, wx.ID_ANY,  publishYear, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.publishedYear, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.page1, wx.ID_ANY, u"Finding Aid Author:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer1.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.faAuthor = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.faAuthor, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.page1, wx.ID_ANY, u"Finding Aid Creation Date Normal:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer1.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.faDate = wx.TextCtrl( self.page1, wx.ID_ANY,  faCreationDate, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.faDate, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self.page1, wx.ID_ANY, u"Extent:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer1.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.collectionExtent = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer141.Add( self.collectionExtent, 0, wx.ALL, 5 )
		
		self.extentUnitChoices = ["cubic ft.", "GB", "MB", "KB", "vol."]
		self.collectionExtentUnit = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.extentUnitChoices, 0 )
		self.collectionExtentUnit.SetSelection( 0 )
		bSizer141.Add( self.collectionExtentUnit, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer141, 1, wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self.page1, wx.ID_ANY, u"Acquisition Information:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer1.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.acquisition = wx.TextCtrl( self.page1, wx.ID_ANY,  acqInfo, wx.DefaultPosition, wx.Size( 350, 75 ), wx.TE_MULTILINE )
		fgSizer1.Add( self.acquisition, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self.page1, wx.ID_ANY, u"Acquisition Date Normal:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer1.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.acquisitionDate = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.acquisitionDate, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self.page1, wx.ID_ANY, u"Arrangement:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		fgSizer1.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.collectionArrangement = wx.TextCtrl( self.page1, wx.ID_ANY,  arrangeStmt, wx.DefaultPosition, wx.Size( 350, 75 ), wx.TE_MULTILINE )
		fgSizer1.Add( self.collectionArrangement, 0, wx.ALL, 5 )
		
		self.access = wx.StaticText( self.page1, wx.ID_ANY, u"Access Statement:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.access.Wrap( -1 )
		fgSizer1.Add( self.access, 0, wx.ALL, 5 )
		
		self.collectionAccess = wx.TextCtrl( self.page1, wx.ID_ANY,  accessStmt, wx.DefaultPosition, wx.Size( 350, 75 ), wx.TE_MULTILINE )
		fgSizer1.Add( self.collectionAccess, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.page1, wx.ID_ANY, u"Use Statement:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer1.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.collectionUse = wx.TextCtrl( self.page1, wx.ID_ANY,  useStmt, wx.DefaultPosition, wx.Size( 350, 75 ), wx.TE_MULTILINE )
		fgSizer1.Add( self.collectionUse, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer81 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer3 = wx.FlexGridSizer( 2, 2, 0, 0 )
		
		self.m_staticText15 = wx.StaticText( self.page1, wx.ID_ANY, u"Revisions:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, True, wx.EmptyString ) )
		
		gSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		gSizer4 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.newEvent = wx.StaticText( self.page1, wx.ID_ANY, u"Event", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.newEvent.Wrap( -1 )
		self.newEvent.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		gSizer4.Add( self.newEvent, 0, wx.ALL, 5 )
		
		self.newDate = wx.StaticText( self.page1, wx.ID_ANY, u"Normal Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.newDate.Wrap( -1 )
		self.newDate.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		gSizer4.Add( self.newDate, 0, wx.ALL, 5 )
		
		self.addEvent = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gSizer4.Add( self.addEvent, 0, wx.ALL, 5 )
		
		self.addRevisionDate = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		gSizer4.Add( self.addRevisionDate, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		revisionSize = wx.BoxSizer( wx.VERTICAL )
		
		self.addRevision = wx.Button( self.page1, wx.ID_ANY, u"Add Revision >", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.removeRevision = wx.Button( self.page1, wx.ID_ANY, u"Remove Revision <", wx.DefaultPosition, wx.DefaultSize, 0 )
		revisionSize.Add( self.addRevision, 0, wx.ALL, 5 )
		revisionSize.Add( self.removeRevision, 0, wx.ALL, 5 )
		
		gSizer3.Add( revisionSize, 1, wx.EXPAND, 5 )
		
		self.revisionReference = []
		
		self.revisionList = wx.ListCtrl( self.page1, size=( 350,100), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
		self.revisionList.InsertColumn(0, 'Date', width=60)
		self.revisionList.InsertColumn(1, 'Revision', width=286)
		self.revisionIndex = 0
		gSizer3.Add( self.revisionList, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		bSizer88 = wx.BoxSizer( wx.VERTICAL )
			
		self.m_staticText241 = wx.StaticText( self.page1, wx.ID_ANY, u"Languages in Collection:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText241.Wrap( -1 )
		self.m_staticText241.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, True, wx.EmptyString ) )
		
		bSizer88.Add( self.m_staticText241, 0, wx.ALL, 5 )
		
		gSizer11 = wx.BoxSizer( wx.HORIZONTAL )
				
		
		self.english = wx.CheckBox( self.page1, wx.ID_ANY, u"English", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.english.SetValue(True) 
		gSizer11.Add( self.english, 0, wx.ALL, 5 )
		
		self.german = wx.CheckBox( self.page1, wx.ID_ANY, u"German", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.german, 0, wx.ALL, 5 )
		
		self.spanish = wx.CheckBox( self.page1, wx.ID_ANY, u"Spanish", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.spanish, 0, wx.ALL, 5 )
		
		self.french = wx.CheckBox( self.page1, wx.ID_ANY, u"French", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.french, 0, wx.ALL, 5 )
		
		self.dutch = wx.CheckBox( self.page1, wx.ID_ANY, u"Dutch", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.dutch, 0, wx.ALL, 5 )
		
		self.italian = wx.CheckBox( self.page1, wx.ID_ANY, u"Italian", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.italian, 0, wx.ALL, 5 )
		
		
		
		bSizer88.Add( gSizer11, 1, wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer88.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )		
		
		bSizer13.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer81.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self.page1, wx.ID_ANY, u"Creator:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		self.m_staticText25.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, True, wx.EmptyString ) )
		
		bSizer88.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		gSizer9 = wx.FlexGridSizer( 2, 3, 0, 0 )
		
		self.m_staticText261 = wx.StaticText( self.page1, wx.ID_ANY, u"Element Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText261.Wrap( -1 )
		self.m_staticText261.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		gSizer9.Add( self.m_staticText261, 0, wx.ALL, 5 )
		
		self.m_staticText271 = wx.StaticText( self.page1, wx.ID_ANY, u"Creator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText271.Wrap( -1 )
		self.m_staticText271.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		gSizer9.Add( self.m_staticText271, 0, wx.ALL, 5 )
		
		self.m_staticText281 = wx.StaticText( self.page1, wx.ID_ANY, u"Source", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )
		self.m_staticText281.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		gSizer9.Add( self.m_staticText281, 0, wx.ALL, 5 )
		
		creatorElementChoices = ["persname", "corpname"]
		self.creatorElement = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, creatorElementChoices, 0 )
		self.creatorElement.SetSelection( 0 )
		gSizer9.Add( self.creatorElement, 0, wx.ALL, 5 )
		
		self.creator = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer9.Add( self.creator, 0, wx.ALL, 5 )
		
		creatorSourceChoices = ["lcsh", "local"]
		self.creatorSource = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, creatorSourceChoices, 0 )
		self.creatorSource.SetSelection( 0 )
		gSizer9.Add( self.creatorSource, 0, wx.ALL, 5 )
		
		
		bSizer88.Add( gSizer9, 1, wx.EXPAND, 5 )
		bSizer81.Add( bSizer88, 1, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.page1, wx.ID_ANY, u"Controlled Access Headings:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		self.m_staticText30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, True, wx.EmptyString ) )
		
		bSizer4.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		gSizer10 = wx.FlexGridSizer( 11, 3, 0, 0 )
		
		self.m_staticText31 = wx.StaticText( self.page1, wx.ID_ANY, u"Element Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		self.m_staticText31.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		gSizer10.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self.page1, wx.ID_ANY, u"Heading", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		self.m_staticText32.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		gSizer10.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self.page1, wx.ID_ANY, u"Source", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		self.m_staticText33.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		gSizer10.Add( self.m_staticText33, 0, wx.ALL, 5 )
		
		elementChoices = ["persname", "corpname", "subject", "geogname", "famname", "title", "genreform"]
		self.element1 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, elementChoices, 0 )
		self.element1.SetSelection( 0 )
		gSizer10.Add( self.element1, 0, wx.ALL, 5 )
		
		self.heading1 = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer10.Add( self.heading1, 0, wx.ALL, 5 )
		
		sourceChoices = ["lcsh", "local", "aat", "meg"]
		self.source1 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sourceChoices, 0 )
		self.source1.SetSelection( 0 )
		gSizer10.Add( self.source1, 0, wx.ALL, 5 )
		
		self.element2 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, elementChoices, 0 )
		self.element2.SetSelection( 0 )
		gSizer10.Add( self.element2, 0, wx.ALL, 5 )
		
		self.heading2 = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer10.Add( self.heading2, 0, wx.ALL, 5 )
		
		self.source2 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sourceChoices, 0 )
		self.source2.SetSelection( 0 )
		gSizer10.Add( self.source2, 0, wx.ALL, 5 )
		
		self.element3 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, elementChoices, 0 )
		self.element3.SetSelection( 0 )
		gSizer10.Add( self.element3, 0, wx.ALL, 5 )
		
		self.heading3 = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer10.Add( self.heading3, 0, wx.ALL, 5 )
		
		self.source3 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sourceChoices, 0 )
		self.source3.SetSelection( 0 )
		gSizer10.Add( self.source3, 0, wx.ALL, 5 )
		
		self.element4 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, elementChoices, 0 )
		self.element4.SetSelection( 0 )
		gSizer10.Add( self.element4, 0, wx.ALL, 5 )
		
		self.heading4 = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer10.Add( self.heading4, 0, wx.ALL, 5 )
		
		self.source4 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sourceChoices, 0 )
		self.source4.SetSelection( 0 )
		gSizer10.Add( self.source4, 0, wx.ALL, 5 )
		
		self.element5 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, elementChoices, 0 )
		self.element5.SetSelection( 0 )
		gSizer10.Add( self.element5, 0, wx.ALL, 5 )
		
		self.heading5 = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer10.Add( self.heading5, 0, wx.ALL, 5 )
		
		self.source5 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sourceChoices, 0 )
		self.source5.SetSelection( 0 )
		gSizer10.Add( self.source5, 0, wx.ALL, 5 )
		
		element6Choices = []
		self.element6 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, elementChoices, 0 )
		self.element6.SetSelection( 0 )
		gSizer10.Add( self.element6, 0, wx.ALL, 5 )
		
		self.heading6 = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer10.Add( self.heading6, 0, wx.ALL, 5 )
		
		source6Choices = []
		self.source6 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sourceChoices, 0 )
		self.source6.SetSelection( 0 )
		gSizer10.Add( self.source6, 0, wx.ALL, 5 )
		
		element7Choices = []
		self.element7 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, elementChoices, 0 )
		self.element7.SetSelection( 0 )
		gSizer10.Add( self.element7, 0, wx.ALL, 5 )
		
		self.heading7 = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer10.Add( self.heading7, 0, wx.ALL, 5 )
		
		source7Choices = []
		self.source7 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sourceChoices, 0 )
		self.source7.SetSelection( 0 )
		gSizer10.Add( self.source7, 0, wx.ALL, 5 )
		
		element8Choices = []
		self.element8 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, elementChoices, 0 )
		self.element8.SetSelection( 0 )
		gSizer10.Add( self.element8, 0, wx.ALL, 5 )
		
		self.heading8 = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer10.Add( self.heading8, 0, wx.ALL, 5 )
		
		source8Choices = []
		self.source8 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sourceChoices, 0 )
		self.source8.SetSelection( 0 )
		gSizer10.Add( self.source8, 0, wx.ALL, 5 )
		
		element9Choices = []
		self.element9 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, elementChoices, 0 )
		self.element9.SetSelection( 0 )
		gSizer10.Add( self.element9, 0, wx.ALL, 5 )
		
		self.heading9 = wx.TextCtrl( self.page1, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		gSizer10.Add( self.heading9, 0, wx.ALL, 5 )
		
		source9Choices = []
		self.source9 = wx.Choice( self.page1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sourceChoices, 0 )
		self.source9.SetSelection( 0 )
		gSizer10.Add( self.source9, 0, wx.ALL, 5 )
		
		
		
		bSizer4.Add( gSizer10, 1, wx.EXPAND, 5 )
		
		
		bSizer16.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer81.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer81, 1, wx.EXPAND, 5 )
		
		
		self.page1.SetSizer( bSizer5 )
		self.page1.Layout()
		bSizer5.Fit( self.page1 )
		self.page2.AddPage( self.page1, u"Collection Information", True )
		self.m_panel5 = wx.Panel( self.page2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText331 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Abstract:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText331.Wrap( -1 )
		self.m_staticText331.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, True, wx.EmptyString ) )
		
		bSizer131.Add( self.m_staticText331, 0, wx.ALL, 5 )
		
		self.abstract = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 600, 75 ), wx.TE_MULTILINE )
		bSizer131.Add( self.abstract, 0, wx.ALL, 5 )
		
		self.m_staticline5 = wx.StaticLine( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer131.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText37 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Historical Note:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		self.m_staticText37.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, True, wx.EmptyString ) )
		
		bSizer20.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		
		bSizer20.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText39 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Label:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer20.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.historicalLabel = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  histNoteLabel, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer20.Add( self.historicalLabel, 0, wx.ALL, 5 )
		
		
		bSizer131.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		self.historicalNote = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 600, 270 ), wx.TE_MULTILINE )
		bSizer131.Add( self.historicalNote, 0, wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer131.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Scope and Content Note:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		self.m_staticText38.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, True, wx.EmptyString ) )
		
		bSizer131.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.scopeNote = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 600, 270 ), wx.TE_MULTILINE )
		bSizer131.Add( self.scopeNote, 0, wx.ALL, 5 )
		
		
		bSizer12.Add( bSizer131, 1, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText35 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Collection Contents:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		self.m_staticText35.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, True, wx.EmptyString ) )
		
		bSizer14.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.seriesList = wx.ListCtrl( self.m_panel5, size=( 450, 150), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
		self.seriesList.InsertColumn(0, '#', width=50)
		self.seriesList.InsertColumn(1, 'Series', width=392)
		self.seriesIndex = 0
		bSizer14.Add( self.seriesList, 0, wx.ALL, 5 )
		
		self.seriesReference = []
		
		self.deleteSeries = wx.Button( self.m_panel5, wx.ID_ANY, u"Delete Selected Series", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.deleteSeries, 0, wx.ALL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 7, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText36 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Series:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer2.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.seriesName = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer2.Add( self.seriesName, 0, wx.ALL, 5 )
		
		self.m_staticText371 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Series #:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )
		fgSizer2.Add( self.m_staticText371, 0, wx.ALL, 5 )
		
		self.seriesNumber = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer2.Add( self.seriesNumber, 0, wx.ALL, 5 )
		
		self.m_staticText381 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Normal Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText381.Wrap( -1 )
		fgSizer2.Add( self.m_staticText381, 0, wx.ALL, 5 )
		
		self.seriesNormal = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer2.Add( self.seriesNormal, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Extent:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer2.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.seriesExtent = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		bSizer15.Add( self.seriesExtent, 0, wx.ALL, 5 )
		
		self.seriesExtentUnits = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.extentUnitChoices, 0 )
		self.seriesExtentUnits.SetSelection( 0 )
		bSizer15.Add( self.seriesExtentUnits, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		self.m_staticText391 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Scope and Content:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText391.Wrap( -1 )
		fgSizer2.Add( self.m_staticText391, 0, wx.ALL, 5 )
		
		self.seriesScope = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400, 90 ), wx.TE_MULTILINE )
		fgSizer2.Add( self.seriesScope, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Arrangement:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		fgSizer2.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.seriesArrangement = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400, 90 ), wx.TE_MULTILINE )
		fgSizer2.Add( self.seriesArrangement, 0, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Access:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		fgSizer2.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.seriesAccess = wx.TextCtrl( self.m_panel5, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.Size( 400, 90 ), wx.TE_MULTILINE )
		fgSizer2.Add( self.seriesAccess, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		self.addSeries = wx.Button( self.m_panel5, wx.ID_ANY, u"Add/Update Series", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.addSeries, 0, wx.ALL, 5 )
		
		
		bSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( bSizer12 )
		self.m_panel5.Layout()
		bSizer12.Fit( self.m_panel5 )
		self.page2.AddPage( self.m_panel5, u"More Details", False )
		
		bSizer2.Add( self.page2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		self.Bind( wx.EVT_CLOSE, self.closeWindow )
		self.Bind(wx.EVT_MENU, self.Export_EAD, self.saveAs)
		self.addRevision.Bind( wx.EVT_BUTTON, self.Add_Revision )
		self.removeRevision.Bind( wx.EVT_BUTTON, self.Remove_Revision )
		self.deleteSeries.Bind( wx.EVT_BUTTON, self.Delete_Series )
		self.addSeries.Bind( wx.EVT_BUTTON, self.Update_Series )
		self.seriesList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.Show_Series )
	
	def __del__( self ):
		pass
	
	def closeWindow( self, event ):
		sys.exit()
