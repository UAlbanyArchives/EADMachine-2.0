#importing wx files
import wx
from lxml import etree as ET
import traceback
import sys
import re
from operator import itemgetter

 
#import the newly created GUI file
import machineGUI as gui
 
 
#inherit from the MainFrame created in wxFormBuilder and create ANTSFrame
class MachineFrame(gui.mainFrame):
	#constructor
	def __init__(self, parent):
		
	
		
			
		#initialize parent class
		try:
			gui.mainFrame.__init__(self, parent)
		except:
			exceptMsg = traceback.format_exc()
			print exceptMsg
			
	def Check_Normal(self, dateNormal):
		issueCount = 0
		issueString = "Normal Date is invalid"
		if re.search('[a-zA-Z]', dateNormal):
			issueCount = issueCount + 1
			issueString.append("Normal Date is incorrect, contains alphabetical characters.")
		normalLength = (4, 7, 9, 10, 12, 15, 18, 21)
		if not len(dateNormal) in normalLength:
			issueCount = issueCount + 1
		else:
			if len(dateNormal) > 4:
				if "/" in dateNormal:
					if dateNormal.count('/') > 1:
						issueCount = issueCount + 1
				elif "-" in dateNormal:
					if len(dateNormal) == 7 or len(dateNormal) == 10:
						pass
					else:
						issueCount = issueCount + 1
				else:
					issueCount = issueCount + 1
			if len(dateNormal) == 9:
				if "-" in dateNormal:
					if dateNormal.count('-') == 1:
						if len(dateNormal.split('-')[0]) != 4 or len(dateNormal.split('-')[1]) != 4:
							issueCount = issueCount + 1
					elif dateNormal.count('-') == 2:
						if len(dateNormal.split('-')[0]) != 4 or len(dateNormal.split('-')[1]) != 2 or len(dateNormal.split('-')[3]) != 2:
							issueCount = issueCount + 1
					else:
						issueCount = issueCount + 1
				elif "/" in dateNormal:
					if len(dateNormal.split('/')[0]) != 4 or len(dateNormal.split('/')[1]) != 4:
						issueCount = issueCount + 1
				else:
					issueCount = issueCount + 1
			elif len(dateNormal) == 7:
				if "-" in dateNormal:
					if len(dateNormal.split('-')[0]) != 4 or len(dateNormal.split('-')[1]) != 2:
						issueCount = issueCount + 1
				else:
					issueCount = issueCount + 1
		if issueCount != 0:
			normalError = wx.MessageDialog(None, issueString, "ERROR", wx.OK | wx.ICON_ERROR)
			normalError.ShowModal()
			return False
		else:
			return True
 
	def Add_Revision(self, event):
		if len(self.addEvent.GetValue()) > 0:
			newEvent = self.addEvent.GetValue().strip()
			newRevisionDate = self.addRevisionDate.GetValue().strip()
			if self.Check_Normal(newRevisionDate) is True:
				self.revisionReference.append({"event": newEvent, "date": newRevisionDate})
				self.revisionList.InsertStringItem(self.revisionIndex, newRevisionDate)
				self.revisionList.SetStringItem(self.revisionIndex, 1, newEvent)
				self.revisionIndex += 1
				self.addEvent.SetValue("")
				self.addRevisionDate.SetValue("")
			
	def Remove_Revision(self, event):
		selectRevision = self.revisionList.GetFirstSelected()
		if selectRevision != -1:
			removeDate = self.revisionList.GetItemText(selectRevision, 0)
			removeEvent = self.revisionList.GetItemText(selectRevision, 1)
			self.revisionReference[:] = [d for d in self.revisionReference if d.get('date') != removeDate or d.get('event') != removeEvent]
			self.revisionList.DeleteItem(selectRevision)
			self.revisionIndex  = self.revisionIndex - 1
	
	def Update_Series(self, event):
		if len(self.seriesName.GetValue()) > 0:
			try:
				float(self.seriesNumber.GetValue())
			except:
				seriesWrong = wx.MessageDialog(None, "The series number you added is not valid.", "Series Number Invalid", wx.OK | wx.ICON_WARNING)
				seriesWrong.ShowModal()		
			if len(self.seriesNumber.GetValue()) < 1 or len(self.seriesNormal.GetValue()) < 1:
				seriesIncomplete = wx.MessageDialog(None, "The series you added is incomplete. Series # and Normal Date are required.", "Series Incomplete", wx.OK | wx.ICON_WARNING)
				seriesIncomplete.ShowModal()			
			else:
				newSeries = self.seriesName.GetValue().strip()
				newSeriesNumber = self.seriesNumber.GetValue().strip()
				newSeriesDate = self.seriesNormal.GetValue().strip()
				newSeriesExtent = self.seriesExtent.GetValue().strip()
				newSeriesUnit = self.seriesExtentUnits.GetStringSelection()
				newSeriesScope = self.seriesScope.GetValue().strip()
				newSeriesArrangement = self.seriesArrangement.GetValue().strip()
				newSeriesAccess = self.seriesAccess.GetValue().strip()
				if self.Check_Normal(newSeriesDate) is True:
					for checkSeries in self.seriesReference:
						if newSeriesNumber == checkSeries["number"]:
							self.seriesReference[:] = [d for d in self.seriesReference if d.get('number') != newSeriesNumber]
					self.seriesReference.append({"series": newSeries, "number": newSeriesNumber, "date": newSeriesDate, "extent": newSeriesExtent, "unit": newSeriesUnit, "scope": newSeriesScope, "arrange": newSeriesArrangement, "access": newSeriesAccess})
					self.seriesList.DeleteAllItems()
					indexCount = 0
					for series in self.seriesReference:
						self.seriesList.InsertStringItem(indexCount, series["number"])
						self.seriesList.SetStringItem(indexCount, 1, series["series"])
						indexCount = indexCount + 1
					self.seriesName.SetValue("")
					self.seriesNumber.SetValue("")
					self.seriesNormal.SetValue("")
					self.seriesExtent.SetValue("")
					self.seriesExtentUnits.SetSelection(0)
					self.seriesScope.SetValue("")
					self.seriesArrangement.SetValue("")
					self.seriesAccess.SetValue("")

			
	def Show_Series(self, event):
		selectSeries = self.seriesList.GetFirstSelected()
		if selectSeries != -1:
			showSeriesNumber = self.seriesList.GetItemText(selectSeries, 0)
			showSeriesName = self.seriesList.GetItemText(selectSeries, 1)
			matchCount = 0
			for showSeries in self.seriesReference:
				if showSeries["series"] == showSeriesName and showSeries["number"] == showSeriesNumber:
					matchCount = matchCount + 1
					if matchCount > 1:
						showSeriesError = wx.MessageDialog(None, "More than one matching series found. Please delete all series and try again.", "Series Conflict", wx.OK | wx.ICON_WARNING)
						showSeriesError.ShowModal()
					else:
						self.seriesName.SetValue(showSeries["series"])
						self.seriesNumber.SetValue(showSeries["number"])
						self.seriesNormal.SetValue(showSeries["date"])
						self.seriesExtent.SetValue(showSeries["extent"])
						unitIndex = self.extentUnitChoices.index(showSeries["unit"])
						self.seriesExtentUnits.SetSelection(unitIndex)
						self.seriesScope.SetValue(showSeries["scope"])
						self.seriesArrangement.SetValue(showSeries["arrange"])
						self.seriesAccess.SetValue(showSeries["access"])
	
	def Delete_Series(self, event):
		selectSeries = self.seriesList.GetFirstSelected()
		if selectSeries != -1:
			deleteSeriesNumber = self.seriesList.GetItemText(selectSeries)
			deleteSeriesName = self.seriesList.GetItemText(selectSeries, 1)
			self.seriesList.DeleteItem(selectSeries)
			self.seriesReference[:] = [d for d in self.seriesReference if d.get('number') != deleteSeriesNumber]
			self.seriesName.SetValue("")
			self.seriesNumber.SetValue("")
			self.seriesNormal.SetValue("")
			self.seriesExtent.SetValue("")
			self.seriesExtentUnits.SetSelection(0)
			self.seriesScope.SetValue("")
			self.seriesArrangement.SetValue("")
			self.seriesAccess.SetValue("")
			
	def Validate_Input(self):
		issueCount = 0
		issueString = ""
		if len(self.collectionID.GetValue()) < 1:
			issueCount = issueCount + 1
			issueString = issueString + "\nCollection ID is empty."
		if len(self.collectionDate.GetValue()) < 1:
			issueCount = issueCount + 1
			issueString = issueString + "\nCollection Date is empty."
		elif self.Check_Normal(self.collectionDate.GetValue()) is False:
			issueCount = issueCount + 1
			issueString = issueString + "\nCollection Date is not a valid normal date."
		if len(self.processedBy.GetValue()) < 1:
			issueCount = issueCount + 1
			issueString = issueString + "\nProccessed By is empty."
		elif self.processedBy.GetValue().lower() == "unprocessed":
			pass
		elif self.Check_Normal(self.processingDate.GetValue()) is False:
			issueCount = issueCount + 1
			issueString = issueString + "\nProcessing Date is not a valid normal date."
		if len(self.faAuthor.GetValue()) < 1:
			issueCount = issueCount + 1
			issueString = issueString + "\nFinding Aid Author is empty."
		if len(self.collectionExtent.GetValue()) < 1:
			issueCount = issueCount + 1
			issueString = issueString + "\nCollection Extent is empty."
		if len(self.acquisitionDate.GetValue()) > 0:
			if self.Check_Normal(self.acquisitionDate.GetValue()) is False:
				issueCount = issueCount + 1
				issueString = issueString + "\nAcquisition Date is not a valid normal date."
		if len(self.creator.GetValue()) < 1:
			issueCount = issueCount + 1
			issueString = issueString + "\nCreator is empty."
		if len(self.abstract.GetValue()) < 1:
			issueCount = issueCount + 1
			issueString = issueString + "\nAbstract is empty."
		if len(self.historicalNote.GetValue()) < 1:
			issueCount = issueCount + 1
			issueString = issueString + "\nHistorical Note is empty."
		if len(self.historicalLabel.GetValue()) < 1:
			issueCount = issueCount + 1
			issueString = issueString + "\nHistorical Note Label is empty."
		if len(self.scopeNote.GetValue()) < 1:
			issueCount = issueCount + 1
			issueString = issueString + "\nScope and Content Note is empty."
		if issueCount == 0:
			return True
		else:
			inputInvalid = wx.MessageDialog(None, str(issueCount) + " errors:" + issueString, "Input Error", wx.OK | wx.ICON_ERROR)
			inputInvalid.ShowModal()	
			return False
		
	def Display_Date(self, normalDate):
		calendar = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
		if len(normalDate) < 1:
			displayDate = normalDate
		if "/" in normalDate:
			startDate = normalDate.split('/')[0]
			endDate = normalDate.split('/')[1]
			if "-" in startDate:
				if startDate.count('-') == 1:
					startYear = startDate.split("-")[0]
					startMonth = startDate.split("-")[1]
					displayStart = startYear + " " + calendar[startMonth]
				else:
					startYear = startDate.split("-")[0]
					startMonth = startDate.split("-")[1]
					startDay = startDate.split("-")[2]
					if startDay.startswith("0"):
						displayStartDay = startDay[1:]
					else:
						displayStartDay = startDay
					displayStart = startYear + " " + calendar[startMonth] + " " + displayStartDay
			else:
				displayStart = startDate
			if "-" in endDate:
				if endDate.count('-') == 1:
					endYear = endDate.split("-")[0]
					endMonth = endDate.split("-")[1]
					displayEnd = endYear + " " + calendar[endMonth]
				else:
					endYear = endDate.split("-")[0]
					endMonth = endDate.split("-")[1]
					endDay = endDate.split("-")[2]
					if endDay.startswith("0"):
						displayEndDay = endDay[1:]
					else:
						displayEndDay = endDay
					displayEnd = endYear + " " + calendar[endMonth] + " " + displayEndDay
			else:
				displayEnd = endDate
			displayDate = displayStart + "-" + displayEnd
		else:
			if "-" in normalDate:
				if normalDate.count('-') == 1:
					year = normalDate.split("-")[0]
					month = normalDate.split("-")[1]
					displayDate = year + " " + calendar[month]
				else:
					year = normalDate.split("-")[0]
					month = normalDate.split("-")[1]
					day = normalDate.split("-")[2]
					if day.startswith("0"):
						displayDay = day[1:]
					else:
						displayDay = day
					displayDate = year + " " + calendar[month] + " " + displayDay
			else:
				displayDate = normalDate
		return displayDate
	
	def Export_EAD(self, event):
		if self.Validate_Input() is True:
			FABasic = "<ead id=\"\"><eadheader audience=\"external\" countryencoding=\"iso3166-1\" dateencoding=\"iso8601\" findaidstatus=\"new\" langencoding=\"iso639-2b\" relatedencoding=\"DC\" repositoryencoding=\"iso15511\" scriptencoding=\"iso15924\"><eadid countrycode=\"US\" identifier=\"##\" mainagencycode=\"nalsu\" url=\"http://library.albany.edu/speccoll/findaids/eresources/findingaids/\"></eadid><filedesc><titlestmt><titleproper><date normal=\"\" type=\"inclusive\"></date></titleproper><author></author></titlestmt><publicationstmt><publisher>M. E. Grenander Department of Special Collections and Archives</publisher><address><addressline>1400 Washington Avenue / Albany, New York 12222</addressline></address><date normal=\"\" type=\"publication\"></date></publicationstmt></filedesc><profiledesc><creation><date normal=\"\"></date></creation><langusage><language encodinganalog=\"Language\" langcode=\"eng\">English</language></langusage></profiledesc><revisiondesc></revisiondesc></eadheader><frontmatter><titlepage><titleproper><date normal=\"\" type=\"inclusive\"></date></titleproper><publisher></publisher><date type=\"publication\"></date><p>For reference queries contact Grenander Department Reference staff or (518)-437-3934</p></titlepage></frontmatter><archdesc level=\"collection\"><did><head>Descriptive Summary</head><unitid></unitid><unittitle><unitdate label=\"Date:\" normal=\"\" type=\"inclusive\"></unitdate></unittitle><abstract label=\"Abstract:\"></abstract><langmaterial></langmaterial><origination></origination><physdesc><extent unit=\"\"></extent></physdesc><physloc label=\"Storage:\">The materials are located onsite in the department.</physloc><repository label=\"Repository:\"><corpname encodinganalog=\"610\" source=\"local\">M. E. Grenander Department of Special Collections and Archives, University at Albany, SUNY</corpname></repository></did><accessrestrict><head>Access</head></accessrestrict><userestrict><head>Copyright</head></userestrict><acqinfo><head>Acquisition Information</head></acqinfo><bioghist><head></head></bioghist><scopecontent><head>Scope and Content Information</head></scopecontent><arrangement encodinganalog=\"351$a\"><head>Arrangement of the Collection</head></arrangement><prefercite><head>Preferred Citation</head><p>Preferred citation for this material is as follows:</p></prefercite><controlaccess><head>Subject and Genre Headings</head></controlaccess></archdesc></ead>"
			FA = ET.fromstring(FABasic)
			
			coll_ID = "nam_" + self.collectionID.GetValue()
			collectionTitle = self.collectionName.GetValue()
			normalDate = self.collectionDate.GetValue()
			
			#<eadheader>
			FA.set("id", coll_ID)
			FA.find("eadheader/eadid").text = coll_ID
			FA.find("eadheader/eadid").set("url", "http://library.albany.edu/speccoll/findaids/eresources/findingaids/" + coll_ID[4:] + ".html")
			FA.find("eadheader/filedesc/titlestmt/titleproper").text = collectionTitle.upper() + " (" + coll_ID[4:].upper() + ")"
			FA.find("eadheader/filedesc/titlestmt/titleproper/date").text = self.Display_Date(normalDate)
			FA.find("eadheader/filedesc/titlestmt/titleproper/date").set("normal", normalDate)
			FA.find("eadheader/filedesc/titlestmt/author").text = self.processedBy.GetValue()
			if len(self.sponsor.GetValue()) > 0:
				spon = ET.Element("sponsor")
				spon.text = self.sponsor.GetValue()
				FA.find("eadheader/filedesc/titlestmt").append(spon)
			FA.find("eadheader/filedesc/publicationstmt/date").text = "Copyright " + self.Display_Date(self.processingDate.GetValue()) + " By the University at Albany, SUNY. All rights reserved."
			FA.find("eadheader/filedesc/publicationstmt/date").set("normal", self.processingDate.GetValue())
			FA.find("eadheader/profiledesc/creation").text = self.faAuthor.GetValue()
			FA.find("eadheader/profiledesc/creation/date").text = self.Display_Date(self.faDate.GetValue())
			FA.find("eadheader/profiledesc/creation/date").set("normal", self.faDate.GetValue())
			for revision in self.revisionReference:
				change = ET.SubElement(FA.find("eadheader/revisiondesc"), "change")
				dateRevision = ET.SubElement(change, "date")
				itemRevision = ET.SubElement(change, "item")
				dateRevision.text = self.Display_Date(revision["date"])
				dateRevision.set("normal", revision["date"])
				itemRevision.text = revision["event"]
			if len(self.revisionReference) < 1:
				FA.find("eadheader").remove(FA.find("eadheader/revisiondesc"))
			
			FA.find("frontmatter/titlepage/titleproper").text = collectionTitle
			FA.find("frontmatter/titlepage/titleproper/date").text = self.Display_Date(normalDate)
			FA.find("frontmatter/titlepage/titleproper/date").set("normal", normalDate)
			FA.find("frontmatter/titlepage/date").text = "Copyright " + self.publishedYear.GetValue() + " By the University at Albany, SUNY. All rights reserved."
			
			#<archdesc>/<did>
			FA.find("archdesc/did/unitid").text = coll_ID
			FA.find("archdesc/did/unittitle").text = collectionTitle
			FA.find("archdesc/did/unittitle/unitdate").text = self.Display_Date(normalDate)
			FA.find("archdesc/did/unittitle/unitdate").set("normal", normalDate)
			FA.find("archdesc/did/abstract").text = self.abstract.GetValue()
			FA.find("archdesc/did/physdesc/extent").text = self.collectionExtent.GetValue()
			FA.find("archdesc/did/physdesc/extent").set("unit", self.collectionExtentUnit.GetStringSelection())
			langMaterial = FA.find("archdesc/did/langmaterial")
			if self.english.IsChecked():
				newLang = ET.SubElement(langMaterial, "language")
				newLang.text = "English"
				newLang.set("langcode", "eng")
			if self.german.IsChecked():
				newLang = ET.SubElement(langMaterial, "language")
				newLang.text = "German"
				newLang.set("langcode", "ger")
			if self.spanish.IsChecked():
				newLang = ET.SubElement(langMaterial, "language")
				newLang.text = "Spanish"
				newLang.set("langcode", "spa")
			if self.french.IsChecked():
				newLang = ET.SubElement(langMaterial, "language")
				newLang.text = "French"
				newLang.set("langcode", "fre")
			if self.dutch.IsChecked():
				newLang = ET.SubElement(langMaterial, "language")
				newLang.text = "Dutch"
				newLang.set("langcode", "dut")
			if self.italian.IsChecked():
				newLang = ET.SubElement(langMaterial, "language")
				newLang.text = "Italian"
				newLang.set("langcode", "ita")
			origin = FA.find("archdesc/did/origination")
			creator = self.creatorElement.GetStringSelection()
			if creator == "persname":
				originator = ET.SubElement(origin, "persname")
				originator.text = self.creator.GetValue()
				originator.set("encodinganalog", "100")
				originator.set("source", self.creatorSource.GetStringSelection())
			elif creator == "corpname":
				originator = ET.SubElement(origin, "corpname")
				originator.text = self.creator.GetValue()
				originator.set("encodinganalog", "110")
				originator.set("source", self.creatorSource.GetStringSelection())
				
			#<archdesc>
			if self.collectionAccess.GetValue().startswith("<p>"):
				FA.find("archdesc/accessrestrict/head").tail = self.collectionAccess.GetValue()
			else:
				accessRestrict = ET.Element("p")
				accessRestrict.text = self.collectionAccess.GetValue()
				FA.find("archdesc/userestrict").append(accessRestrict)
				
			if self.collectionUse.GetValue().startswith("<p>"):
				FA.find("archdesc/userestrict/head").tail = self.collectionUse.GetValue()
			else:
				useRestrict = ET.Element("p")
				useRestrict.text = self.collectionUse.GetValue()
				FA.find("archdesc/userestrict").append(useRestrict)
				
			acq = ET.Element("p")
			FA.find("archdesc/acqinfo").append(acq)
			if len(self.acquisitionDate.GetValue()) > 0:
				acqDate = ET.SubElement(acq, "date")
				acqDate.text = self.Display_Date(self.acquisitionDate.GetValue())
				acqDate.set("normal", self.acquisitionDate.GetValue())
			acq.text = self.acquisition.GetValue()
			
			FA.find("archdesc/bioghist/head").text = self.historicalLabel.GetValue()
			if self.historicalNote.GetValue().startswith("<p>"):
				FA.find("archdesc/bioghist/head").tail = self.historicalNote.GetValue().strip()
			else:
				biogNote = ET.Element("p")
				biogNote.text = self.historicalNote.GetValue()
				FA.find("archdesc/bioghist").append(biogNote)
				
			if self.scopeNote.GetValue().startswith("<p>"):
				FA.find("archdesc/scopecontent/head").tail = self.scopeNote.GetValue().strip()
			else:
				scope = ET.Element("p")
				scope.text = self.scopeNote.GetValue()
				FA.find("archdesc/scopecontent").append(scope)
				
			if self.collectionArrangement.GetValue().startswith("<p>"):
				FA.find("archdesc/arrangement/head").tail = self.collectionArrangement.GetValue().strip()
			else:
				arr = ET.Element("p")
				arr.text = self.collectionArrangement.GetValue()
				FA.find("archdesc/arrangement").append(arr)
			
			prefCite = ET.Element("p")
			prefCite.text = "Identification of specific item, series, box, folder, " + collectionTitle + ", " + self.Display_Date(normalDate) + ". M.E. Grenander Department of Special Collections and Archives, University  Libraries, University at Albany, State University of New York (hereafter referred to as the " + collectionTitle + ")."
			FA.find("archdesc/prefercite").append(prefCite)
			
			#<controlaccess>
			controlAccess = FA.find("archdesc/controlaccess")
			if len(self.heading1.GetValue()) > 0:
				accessPoint1 = ET.SubElement(controlAccess, self.element1.GetStringSelection())
				accessPoint1.text = self.heading1.GetValue()
				accessPoint1.set("source", self.source1.GetStringSelection())
			if len(self.heading2.GetValue()) > 0:
				accessPoint2 = ET.SubElement(controlAccess, self.element2.GetStringSelection())
				accessPoint2.text = self.heading2.GetValue()
				accessPoint2.set("source", self.source2.GetStringSelection())
			if len(self.heading3.GetValue()) > 0:
				accessPoint3 = ET.SubElement(controlAccess, self.element3.GetStringSelection())
				accessPoint3.text = self.heading3.GetValue()
				accessPoint3.set("source", self.source3.GetStringSelection())
			if len(self.heading4.GetValue()) > 0:
				accessPoint4 = ET.SubElement(controlAccess, self.element4.GetStringSelection())
				accessPoint4.text = self.heading4.GetValue()
				accessPoint4.set("source", self.source4.GetStringSelection())
			if len(self.heading5.GetValue()) > 0:
				accessPoint5 = ET.SubElement(controlAccess, self.element5.GetStringSelection())
				accessPoint5.text = self.heading5.GetValue()
				accessPoint5.set("source", self.source5.GetStringSelection())
			if len(self.heading6.GetValue()) > 0:
				accessPoint6 = ET.SubElement(controlAccess, self.element6.GetStringSelection())
				accessPoint6.text = self.heading6.GetValue()
				accessPoint6.set("source", self.source6.GetStringSelection())
			if len(self.heading7.GetValue()) > 0:
				accessPoint7 = ET.SubElement(controlAccess, self.element7.GetStringSelection())
				accessPoint7.text = self.heading7.GetValue()
				accessPoint7.set("source", self.source7.GetStringSelection())
			if len(self.heading8.GetValue()) > 0:
				accessPoint8 = ET.SubElement(controlAccess, self.element8.GetStringSelection())
				accessPoint8.text = self.heading8.GetValue()
				accessPoint8.set("source", self.source8.GetStringSelection())
			if len(self.heading9.GetValue()) > 0:
				accessPoint9 = ET.SubElement(controlAccess, self.element9.GetStringSelection())
				accessPoint9.text = self.heading9.GetValue()
				accessPoint9.set("source", self.source9.GetStringSelection())
			for accessPoint in FA.find("archdesc/controlaccess"):
				if accessPoint.tag == "persname":
					accessPoint.set("encodinganalog", "600")
				elif accessPoint.tag == "corpname":
					accessPoint.set("encodinganalog", "610")
				elif accessPoint.tag == "subject":
					accessPoint.set("encodinganalog", "650")
				elif accessPoint.tag == "geogname":
					accessPoint.set("encodinganalog", "651")
				elif accessPoint.tag == "famname":
					accessPoint.set("encodinganalog", "600")
				elif accessPoint.tag == "title":
					accessPoint.set("encodinganalog", "630")
				elif accessPoint.tag == "genreform":
					accessPoint.set("encodinganalog", "655")
				else:
					pass
			
			#<dsc>
			if len(self.seriesReference) > 0:
				dsc = ET.Element("dsc")
				FA.find("archdesc").append(dsc)
				dscHead = ET.Element("head")
				dscHead.text = "Container List"
				dsc.insert(0, dscHead)
				seriesSorted = sorted(self.seriesReference, key=itemgetter('number'))
				seriesCount = 1
				for series in seriesSorted:
					c01 = ET.Element("c01")
					c01.set("level", "series")
					c01.set("id", coll_ID + "-" + str(seriesCount))
					did = ET.SubElement(c01, "did")
					unitid = ET.SubElement(did, "unitid")
					unitid.text = str(seriesCount)
					unittitle = ET.SubElement(did, "unittitle")
					unittitle.text = series["series"]
					unittitle.set("label", "Series")
					unitdate = ET.SubElement(did, "unitdate")
					unitdate.text = self.Display_Date(series["date"])
					unitdate.set("type", "inclusive")
					unitdate.set("era", "ce")
					unitdate.set("calendar", "gregorian")
					unitdate.set("normal", series["date"])
					if len(series["extent"]) > 0:
						physdesc = ET.SubElement(did, "physdesc")
						extent = ET.SubElement(physdesc, "extent")
						extent.text = series["extent"]
						extent.set("unit", series["unit"])
					if len(series["access"]) > 0:
						accessElement = ET.SubElement(c01, "accessrestrict")
						if series["access"].startswith("<p>"):
							accessElement.text = series["access"].strip()
						else:
							accessP = ET.SubElement(accessElement, "p")
							accessP.text = series["access"].strip()
					if len(series["scope"]) > 0:
						scopeElement = ET.SubElement(c01, "scopecontent")
						if series["scope"].startswith("<p>"):
							scopeElement.text = series["scope"].strip()
						else:
							scopeP = ET.SubElement(scopeElement, "p")
							scopeP.text = series["scope"].strip()
					if len(series["arrange"]) > 0:
						arrangeElement = ET.SubElement(c01, "arrangement")
						if series["arrange"].startswith("<p>"):
							arrangeElement.text = series["arrange"].strip()
						else:
							arrangeP = ET.SubElement(arrangeElement, "p")
							arrangeP.text = series["arrange"].strip()
					dsc.append(c01)
					seriesCount = seriesCount + 1
				
				
			
			FA_string = ET.tostring(FA, pretty_print=True, xml_declaration=True, encoding="utf-8", doctype="<!DOCTYPE ead SYSTEM 'ead.dtd'>")
			FA_string = FA_string.replace("&lt;", "<")
			FA_string = FA_string.replace("&gt;", ">")
		
			#insert stylesheet processing instruction
			if FA.iter("c02") is None:
				FA_output = FA_string[:38] + "\n<?xml-stylesheet type='text/xsl' href='collection-level_no_series.xsl'?> " + FA_string[38:]
			else:
				FA_output = FA_string[:38] + "\n<?xml-stylesheet type='text/xsl' href='collection-level.xsl'?> " + FA_string[38:]
					
			dlg = wx.FileDialog(self, message="Save EAD as ...", defaultDir="", defaultFile= coll_ID[4:] + ".xml", wildcard="XML file(*.xml)|*.*", style=wx.SAVE|wx.OVERWRITE_PROMPT)
			if dlg.ShowModal() == wx.ID_OK:
				output_path = dlg.GetPath()
			dlg.Destroy()
			
			file = open(output_path, "w")
			file.write(FA_output)
			file.close
		
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of ANTSFrame
frame = MachineFrame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()