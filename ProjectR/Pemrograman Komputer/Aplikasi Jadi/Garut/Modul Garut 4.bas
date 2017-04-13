REM  *****  BASIC  *****
SUB SH


c = thiscomponent.currentcontroller.getactivesheet().rangeaddress.sheet
print c

end sub
    REM  *****  BASIC  *****
    REM copy first sheet of this document to position 2 of a new one
    Sub Main
    refresh
    REM source document
    Dim sURL$, sLinkSheetName$
       sURL = thisComponent.getURL()
    
    
    c = thiscomponent.currentcontroller.getactivesheet().rangeaddress.sheet
    sLinkSheetName = thisComponent.Sheets(c).getName()

       
    REM target document
    Dim doc, sheets, sName$, pos%
       doc = StarDesktop.loadComponentFromURL("private:factory/scalc", "_default",0, Array())
       sheets = doc.getSheets()
       sName = getUniqueName(sheets, "Kunjungan Pasien")
       pos = 1

    REM new sheet
    Dim sh
       sheets.insertNewByName(sName, pos)
       sh = sheets.getByName(sName)
       
    REM link the new sheet
       sh.link(sURL, sLinkSheetName, "calc8", "", com.sun.star.sheet.SheetLinkMode.NORMAL)
       

       
    REM break link
       sh.setLinkMode(com.sun.star.sheet.SheetLinkMode.NONE)
       
       
       

    End Sub

    Function getUniqueName(oContainer,sName$)
    Dim i%,sNew$
       sNew = sName
       Do while oContainer.hasByName(sNew)
          i = i + 1
          sNew = sName &"_"& i   
       loop
       getUniqueName = sNew
    End Function
    
    
    
 sub filtra_data()
	doc = thiscomponent
	doc.sheets(4).unprotect ("")
       Dim xRange as object
       Dim FilterDesc as Object
       Dim FilterFields(1) as new com.sun.star.sheet.TableFilterField
       
       Dim data_da
       Dim data_a
       data_da = InputBox("Masukan Tanggal Awal (dd/mm/yyyy): ")
           If data_da = "" Then Exit Sub
       data_a = InputBox("Masukan Tanggal Akhir (dd/mm/yyyy): ")
           If data_a = "" Then Exit Sub

       xRange = thiscomponent.sheets(4).getCellRangeByName("A2:A1048576")
       FilterDesc = xRange.createFilterDescriptor(true)
       
       FilterDesc.ContainsHeader = true
       FilterFields(0).Field = 0
       FilterFields(0).IsNumeric = false
       FilterFields(0).Operator = com.sun.star.sheet.FilterOperator.GREATER_EQUAL
       FilterFields(0).StringValue = data_da
       
       
       FilterFields(1).Field = 0
       FilterFields(1).IsNumeric = false
       FilterFields(1).Operator = com.sun.star.sheet.FilterOperator.LESS_EQUAL
       FilterFields(1).StringValue = data_a
       
       FilterDesc.SetFilterFields(FilterFields)
       
       xRange.Filter(FilterDesc)
	doc.sheets(4).protect ("")
    End Sub


    sub Remove_filter()
        thiscomponent.sheets(4).unprotect ("")
        
         thiscomponent.sheets(4).Rows.Isvisible = true
    	  thiscomponent.sheets(4).protect ("")
        
    end sub
    
    
    
    
    sub copyrange
    Dim Doc As Object
Dim Sheet As Object

 
doc = ThisComponent
Sheet = Doc.Sheets(4)
 
c = doc.sheets(4).getcellrangebyname ("a1:i1048576")
p = doc.sheets(6).getcellrangebyname ("a1")
 
Sheet.copyRange(p.celladdress, c.rangeaddress)

end sub


sub REKAPDATAFILTER()
	doc = thiscomponent
	doc.sheets(4).unprotect ("")
       Dim xRange as object
       Dim FilterDesc as Object
       Dim FilterFields(2) as new com.sun.star.sheet.TableFilterField
       
       doc.sheets(6).getcellrangebyname ("A1:J1048576").ClearContents (1 or 2 or 4 or 8 or 16 or 32 or 64)
       doc.sheets(11).getcellrangebyname ("A1:J1048576").ClearContents (1 or 2 or 4 or 8 or 16 or 32 or 64)
       doc.sheets(12).getcellrangebyname ("A1:J1048576").ClearContents (1 or 2 or 4 or 8 or 16 or 32 or 64)
       doc.sheets(13).getcellrangebyname ("A1:J1048576").ClearContents (1 or 2 or 4 or 8 or 16 or 32 or 64)
       Dim data_da
       Dim data_a
       data_da = doc.sheets(1).getcellrangebyname ("B12").value
           If data_da = "" Then Exit Sub
       data_a = doc.sheets(1).getcellrangebyname ("B13").value
           If data_a = "" Then Exit Sub
	   datapa = doc.sheets(1).getcellrangebyname ("B14").string

       	   
       
       xRange = thiscomponent.sheets(4).getCellRangeByName("A1:F1048576")
       FilterDesc = xRange.createFilterDescriptor(true)
       
       FilterDesc.ContainsHeader = true
       FilterFields(0).Field = 0
       FilterFields(0).IsNumeric = false
       FilterFields(0).Operator = com.sun.star.sheet.FilterOperator.GREATER_EQUAL
       FilterFields(0).StringValue = data_da
       
       
       FilterFields(1).Field = 0
       FilterFields(1).IsNumeric = false
       FilterFields(1).Operator = com.sun.star.sheet.FilterOperator.LESS_EQUAL
       FilterFields(1).StringValue = data_a
      
       If datapa = "" Then
       
       else
       FilterDesc.ContainsHeader = true
       FilterFields(2).Field = 5
       FilterFields(2).IsNumeric = false
       FilterFields(2).Operator = com.sun.star.sheet.FilterOperator.EQUAL
       FilterFields(2).StringValue = datapa
       
       
       end if
       FilterDesc.SetFilterFields(FilterFields)
       
       xRange.Filter(FilterDesc)
       
       REM -----
if datapa = "" then   
	
Sheet = Doc.Sheets(4)
 
c = doc.sheets(4).getcellrangebyname ("A1:J1048576")
p = doc.sheets(6).getcellrangebyname ("A2")
Sheet.copyRange(p.celladdress, c.rangeaddress)

doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(6)
seleksi.setactivesheet (menuju)

else
if datapa = "POLISI" then   
	
Sheet = Doc.Sheets(4)
 
c = doc.sheets(4).getcellrangebyname ("A1:J1048576")
p = doc.sheets(11).getcellrangebyname ("A2")
Sheet.copyRange(p.celladdress, c.rangeaddress)
doc.sheets(11).getcellrangebyname ("H2").string = "NRP"

doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(11)
seleksi.setactivesheet (menuju)

else

if datapa = "PNS" then   
	
Sheet = Doc.Sheets(4)
 
c = doc.sheets(4).getcellrangebyname ("A1:J1048576")
p = doc.sheets(12).getcellrangebyname ("A2")
Sheet.copyRange(p.celladdress, c.rangeaddress)
doc.sheets(12).getcellrangebyname ("H2").string = "NIP"

doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(12)
seleksi.setactivesheet (menuju)
else
if datapa = "UMUM" then   
	
Sheet = Doc.Sheets(4)
c1 = doc.sheets(4).getcellrangebyname ("A1:F1048576")
p1 = doc.sheets(13).getcellrangebyname ("A2")
c = doc.sheets(4).getcellrangebyname ("I1:J1048576")
p = doc.sheets(13).getcellrangebyname ("G2")
Sheet.copyRange(p.celladdress, c.rangeaddress)
Sheet.copyRange(p1.celladdress, c1.rangeaddress)
doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(13)
seleksi.setactivesheet (menuju)

end if
end if
end if
end if
thiscomponent.sheets(4).Rows.Isvisible = true
	
doc.sheets(4).protect ("")
	
End Sub



    Sub refreshAllSheetLinks()
    oEnum = thisComponent.AreaLinks.createEnumeration
    while oEnum.hasMoreElements
       oLink = oEnum.NextElement
       oLink.refresh
    wend
    oEnum = thisComponent.SheetLinks.createEnumeration
    while oEnum.hasMoreElements
       oLink = oEnum.NextElement
       oLink.refresh
    wend
    oEnum = thisComponent.DDELinks.createEnumeration
    while oEnum.hasMoreElements
       oLink = oEnum.NextElement
       oLink.refresh
    wend
    End Sub 
    
    
    

sub refresh
rem ----------------------------------------------------------------------
rem define variables
dim document   as object
dim dispatcher as object
rem ----------------------------------------------------------------------
rem get access to the document
document   = ThisComponent.CurrentController.Frame
dispatcher = createUnoService("com.sun.star.frame.DispatchHelper")

rem ----------------------------------------------------------------------
dispatcher.executeDispatch(document, ".uno:Save", "", 0, Array())


end sub

Sub Main2
    refresh
    REM source document
    Dim sURL$, sLinkSheetName$
       sURL = thisComponent.getURL()
       sLinkSheetName = thisComponent.Sheets(7).getName()

       
    REM target document
    Dim doc, sheets, sName$, pos%
       doc = StarDesktop.loadComponentFromURL("private:factory/scalc", "_default",0, Array())
       sheets = doc.getSheets()
       sName = getUniqueName(sheets, "DataPasien")
       pos = 1

    REM new sheet
    Dim sh
       sheets.insertNewByName(sName, pos)
       sh = sheets.getByName(sName)
       
    REM link the new sheet
       sh.link(sURL, sLinkSheetName, "calc8", "", com.sun.star.sheet.SheetLinkMode.NORMAL)
       

       
    REM break link
       sh.setLinkMode(com.sun.star.sheet.SheetLinkMode.NONE)
       
       
        End Sub
        
        
        
        sub REKAPDATAFILTER2()
		doc = thiscomponent
		doc.sheets(3).unprotect ("")
       Dim xRange as object
       Dim FilterDesc as Object
       Dim FilterFields(0) as new com.sun.star.sheet.TableFilterField
       
       doc.sheets(7).getcellrangebyname ("A1:i1048576").ClearContents (1 or 2 or 4 or 8 )
       
       
       Dim data_da
       Dim data_a
      
	   datapa = doc.sheets(1).getcellrangebyname ("B14").string

       	   
       
       xRange = thiscomponent.sheets(3).getCellRangeByName("A1:e1048576")
       FilterDesc = xRange.createFilterDescriptor(true)
       
             
            
       If datapa = "" Then
       
       else
       FilterDesc.ContainsHeader = true
       FilterFields(0).Field = 3
       FilterFields(0).IsNumeric = false
       FilterFields(0).Operator = com.sun.star.sheet.FilterOperator.EQUAL
       FilterFields(0).StringValue = datapa
       
       
       end if
       FilterDesc.SetFilterFields(FilterFields)
       
       xRange.Filter(FilterDesc)
       
       REM -----
       	
	Sheet = Doc.Sheets(3)
 
c = doc.sheets(3).getcellrangebyname ("a1:i1048576")
p = doc.sheets(7).getcellrangebyname ("a5")

Sheet.copyRange(p.celladdress, c.rangeaddress)

 
doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(7)
seleksi.setactivesheet (menuju)

thiscomponent.sheets(3).Rows.Isvisible = true
	
doc.sheets(3).protect ("")
	
End Sub

sub REKAPDATAFILTERPOLISI()
	doc = thiscomponent
	doc.sheets(3).unprotect ("")
       Dim xRange as object
       Dim FilterDesc as Object
       Dim FilterFields(0) as new com.sun.star.sheet.TableFilterField
       
       doc.sheets(8).getcellrangebyname ("A1:J1048576").ClearContents (1 or 2 or 4 or 8 )
       
       
       Dim data_da
       Dim data_a
      
	   datapa = "POLISI"

       	   
       
       xRange = thiscomponent.sheets(3).getCellRangeByName("A1:F1048576")
       FilterDesc = xRange.createFilterDescriptor(true)
       
             
            
       If datapa = "" Then
       
       else
       FilterDesc.ContainsHeader = true
       FilterFields(0).Field = 4
       FilterFields(0).IsNumeric = false
       FilterFields(0).Operator = com.sun.star.sheet.FilterOperator.EQUAL
       FilterFields(0).StringValue = datapa
       
       
       end if
       FilterDesc.SetFilterFields(FilterFields)
       
       xRange.Filter(FilterDesc)
       
       REM -----
       	
	Sheet = Doc.Sheets(3)
c = doc.sheets(3).getcellrangebyname ("A1:J1048576")
p = doc.sheets(8).getcellrangebyname ("A2")

Sheet.copyRange(p.celladdress, c.rangeaddress)
doc.sheets(8).getcellrangebyname ("G2").string = "NRP"


 
doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(8)
seleksi.setactivesheet (menuju)

thiscomponent.sheets(3).Rows.Isvisible = true
	
doc.sheets(3).protect ("")
	
End Sub

sub REKAPDATAFILTERPNS()
		doc = thiscomponent
		doc.sheets(3).unprotect ("")
       Dim xRange as object
       Dim FilterDesc as Object
       Dim FilterFields(0) as new com.sun.star.sheet.TableFilterField
       
       doc.sheets(9).getcellrangebyname ("A1:J1048576").ClearContents (1 or 2 or 4 or 8 )
       
       
       Dim data_da
       Dim data_a
      
	   datapa = "PNS"

       	   
       
       xRange = thiscomponent.sheets(3).getCellRangeByName("A1:F1048576")
       FilterDesc = xRange.createFilterDescriptor(true)
       
             
            
       If datapa = "" Then
       
       else
       FilterDesc.ContainsHeader = true
       FilterFields(0).Field = 4
       FilterFields(0).IsNumeric = false
       FilterFields(0).Operator = com.sun.star.sheet.FilterOperator.EQUAL
       FilterFields(0).StringValue = datapa
       
       
       end if
       FilterDesc.SetFilterFields(FilterFields)
       
       xRange.Filter(FilterDesc)
       
       REM -----
       	
	Sheet = Doc.Sheets(3)
 
c = doc.sheets(3).getcellrangebyname ("A1:J1048576")
p = doc.sheets(9).getcellrangebyname ("A2")

Sheet.copyRange(p.celladdress, c.rangeaddress)
doc.sheets(9).getcellrangebyname ("G2").string = "NIP"
 
doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(9)
seleksi.setactivesheet (menuju)

thiscomponent.sheets(3).Rows.Isvisible = true
	
doc.sheets(3).protect ("")
	
End Sub

sub REKAPDATAFILTERUMUM()
		doc = thiscomponent
		doc.sheets(3).unprotect ("")
       Dim xRange as object
       Dim FilterDesc as Object
       Dim FilterFields(0) as new com.sun.star.sheet.TableFilterField
       
       doc.sheets(10).getcellrangebyname ("A1:J1048576").ClearContents (1 or 2 or 4 or 8 )
       
       Dim data_da
       Dim data_a
      
	   datapa = "UMUM"

       	   
       
       xRange = thiscomponent.sheets(3).getCellRangeByName("A1:H1048576")
       FilterDesc = xRange.createFilterDescriptor(true)
       
             
            
       If datapa = "" Then
       
       else
       FilterDesc.ContainsHeader = true
       FilterFields(0).Field = 4
       FilterFields(0).IsNumeric = false
       FilterFields(0).Operator = com.sun.star.sheet.FilterOperator.EQUAL
       FilterFields(0).StringValue = datapa
       
       
       end if
       FilterDesc.SetFilterFields(FilterFields)
       
       xRange.Filter(FilterDesc)
       
       REM -----
       	
	Sheet = Doc.Sheets(3)
c1 = doc.sheets(3).getcellrangebyname ("A1:E1048576")
p1= doc.sheets(10).getcellrangebyname ("A2")
c = doc.sheets(3).getcellrangebyname ("H1:I1048576")
p = doc.sheets(10).getcellrangebyname ("F2")

Sheet.copyRange(p.celladdress, c.rangeaddress)
Sheet.copyRange(p1.celladdress,c1.rangeaddress)

 
doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(10)
seleksi.setactivesheet (menuju)

thiscomponent.sheets(3).Rows.Isvisible = true
	
doc.sheets(3).protect ("")
	
End Sub


Sub Mainpolisi
    refresh
    REM source document
    Dim sURL$, sLinkSheetName$
       sURL = thisComponent.getURL()
       sLinkSheetName = thisComponent.Sheets(8).getName()

       
    REM target document
    Dim doc, sheets, sName$, pos%
       doc = StarDesktop.loadComponentFromURL("private:factory/scalc", "_default",0, Array())
       sheets = doc.getSheets()
       sName = getUniqueName(sheets, "DataPasien")
       pos = 1

    REM new sheet
    Dim sh
       sheets.insertNewByName(sName, pos)
       sh = sheets.getByName(sName)
       
    REM link the new sheet
       sh.link(sURL, sLinkSheetName, "calc8", "", com.sun.star.sheet.SheetLinkMode.NORMAL)
       

       
    REM break link
       sh.setLinkMode(com.sun.star.sheet.SheetLinkMode.NONE)
       
       
        End Sub
        
        Sub Mainpns
    refresh
    REM source document
    Dim sURL$, sLinkSheetName$
       sURL = thisComponent.getURL()
       sLinkSheetName = thisComponent.Sheets(9).getName()

       
    REM target document
    Dim doc, sheets, sName$, pos%
       doc = StarDesktop.loadComponentFromURL("private:factory/scalc", "_default",0, Array())
       sheets = doc.getSheets()
       sName = getUniqueName(sheets, "DataPasien")
       pos = 1

    REM new sheet
    Dim sh
       sheets.insertNewByName(sName, pos)
       sh = sheets.getByName(sName)
       
    REM link the new sheet
       sh.link(sURL, sLinkSheetName, "calc8", "", com.sun.star.sheet.SheetLinkMode.NORMAL)
       

       
    REM break link
       sh.setLinkMode(com.sun.star.sheet.SheetLinkMode.NONE)
       
       
        End Sub
        
         Sub Mainumum
    refresh
    REM source document
    Dim sURL$, sLinkSheetName$
       sURL = thisComponent.getURL()
       sLinkSheetName = thisComponent.Sheets(10).getName()

       
    REM target document
    Dim doc, sheets, sName$, pos%
       doc = StarDesktop.loadComponentFromURL("private:factory/scalc", "_default",0, Array())
       sheets = doc.getSheets()
       sName = getUniqueName(sheets, "DataPasien")
       pos = 1

    REM new sheet
    Dim sh
       sheets.insertNewByName(sName, pos)
       sh = sheets.getByName(sName)
       
    REM link the new sheet
       sh.link(sURL, sLinkSheetName, "calc8", "", com.sun.star.sheet.SheetLinkMode.NORMAL)
       

       
    REM break link
       sh.setLinkMode(com.sun.star.sheet.SheetLinkMode.NONE)
       
       
        End Sub
        
        
sub insertdatapasien umum


end sub
