REM  *****  BASIC  *****

Sub Main

End Sub

sub susunjumlahdata
doc = thiscomponent
JumlahData = doc.sheets(1).getcellrangebyname ("A7").string

print (JumlahData)

for i = 1 to i = JumlahData
salin = doc.sheets(3).getcellrangebyname ("a"&i)
tempel = doc.sheets(3).getcellrangebyname ("j"&i)
tempel.dataarray=salin.dataarray

l = tempel.string
print (l)

next

end sub

sub rowdata

doc = thiscomponent
c =doc.sheets(1).getcellrangebyname ("A7").celladdress
l = c.row +1 

print (l)

end sub


sub ulang

doc = thiscomponent
B = doc.sheets(3).getcellrangebyname ("A1")
G =B.string
print (G)
do until  G = ""
i = i + 1
A = doc.sheets(3).getcellrangebyname ("A"&i).celladdress
B = doc.sheets(3).getcellrangebyname ("A"&i)
G = B.string
k = A.row

loop
print (k-1)

end sub


sub tes

l=thiscomponent.sheets(1).RangeAddress.sheet

print (l)

end sub


sub posisirow

doc = thiscomponent
posisi = doc.currentselection.celladdress
 c= posisi.row
print (C)

posisi2= doc.sheets(3).getcellbyposition (0,c)
d = posisi2.string
print (d)
end sub 


sub sebelahkiri
posisi2= doc.sheets(3).getcellbyposition (1,c)


end sub

sub pindah
	oDoc = ThisComponent
	
    c = oDoc.sheets(1).getcellrangebyname ("K3")
 	p = oDoc.sheets(1).getcellrangebyname ("K2")
    p.dataarray=c.dataarray
    salintempel
 
end sub

sub pindah2
oDoc = ThisComponent
	
    c = oDoc.sheets(1).getcellrangebyname ("L3")
 	p = oDoc.sheets(1).getcellrangebyname ("L2")
    p.dataarray=c.dataarray
    salintempel2
    
end sub

sub clear
    oDoc = ThisComponent
	oDoc.sheets(1).getcellrangebyposition(4,1,11,1).ClearContents (1 or 2 or 4 or 8 )
end sub

sub clear2
	clear
    oDoc = ThisComponent
	oDoc.sheets(1).getcellrangebyname("L3").ClearContents (1 or 2 or 4 or 8 )
end sub

sub clear3
	clear
    oDoc = ThisComponent
	oDoc.sheets(1).getcellrangebyname("K3").ClearContents (1 or 2 or 4 or 8 )
end sub


sub salintempel
dim A as string
dim k as boolean
    oDoc = ThisComponent
    L = oDoc.sheets(1).getcellrangebyname ("K2")
    sAns = L.string
    If sAns = "" then End 'Blank entry or Cancel clicked.

	
    oSheet = oDoc.sheets(3).getcellrangebyname ("G2:G1500")'Get active sheet.
    FandR = oSheet.createSearchDescriptor 'Set up find and replace.
    FandR.SearchCaseSensitive = false
	FandR.SearchWords = true
    FandR.setSearchString(sAns)
	FandR.setSearchString(sAns)
    'FandR.SearchWords = true 'Entire cell must match.
        
        oCell = oSheet.findfirst(FandR)

do while not IsNull(oCell)
        c = oCell.celladdress.row

        salin  = oDoc.sheets(3).getcellrangebyposition(0,c,8,c)
		tempel = oDoc.sheets(1).getcellrangebyposition(4,1,12,1)
		tempel.dataarray=salin.dataarray
        if isnull(oCell)     then
        msgbox ("Data tidak ada               ",0,"Informasi")
		oDoc.sheets(1).getcellrangebyposition(4,1,12,1).ClearContents (1 or 2 or 4 or 8 )
		else
		oCell.CharWeight = com.sun.star.awt.FontWeight.BOLD
		oCell = oSheet.findNext( oCell.end, FandR)

		end if
		loop

oDoc.sheets(3).protect ("")

end sub

sub salintempel2
dim A as string
dim k as boolean
    oDoc = ThisComponent
    L = oDoc.sheets(1).getcellrangebyname ("L2")
    sAns = L.string
    If sAns = "" then End 'Blank entry or Cancel clicked.

	oSheet = oDoc.sheets(3).getcellrangebyname ("H2:H1500")'Get active sheet.
    FandR = oSheet.createSearchDescriptor 'Set up find and replace.
    FandR.SearchCaseSensitive = false
	FandR.SearchWords = true
    FandR.setSearchString(sAns)
	FandR.setSearchString(sAns)
    'FandR.SearchWords = true 'Entire cell must match.
        
    oCell = oSheet.findfirst(FandR)

do while not IsNull(oCell)
        c = oCell.celladdress.row

        salin  = oDoc.sheets(3).getcellrangebyposition(0,c,8,c)
		tempel = oDoc.sheets(1).getcellrangebyposition(4,1,12,1)
		tempel.dataarray=salin.dataarray
        if isnull(oCell)     then
        msgbox ("Data tidak ada               ",0,"Informasi")
		oDoc.sheets(1).getcellrangebyposition(4,1,12,1).ClearContents (1 or 2 or 4 or 8 )
		else
		oCell.CharWeight = com.sun.star.awt.FontWeight.BOLD
		oCell = oSheet.findNext( oCell.end, FandR)

		end if
		loop

oDoc.sheets(3).protect ("")

end sub

sub insertdatapasien

doc = thiscomponent

doc.sheets(4).unprotect ("")

k = doc.sheets(1).getcellbyposition (5,1).string

if k = "" then
msgbox ("data tidak ada",0, "Pemberitahuan")
else
oPasteSheet = doc.sheets(4)
pasteRng= oPasteSheet.getcellrangebyposition (0,1,9,1)
oPasteSheet.insertCells(pasteRng.RangeAddress, com.sun.star.sheet.CellInsertMode.DOWN)
Paste = doc.Sheets(4).getcellrangebyposition (0,1,9,1)
Copy  = doc.Sheets(1).getcellrangebyposition (3,1,12,1)
paste.dataarray=copy.dataarray
end if
doc.sheets(1).getcellrangebyposition (3,1,11,1).ClearContents (1 or 2 or 4 or 8 )

doc.sheets(4).protect ("")
end sub

sub bukakunci
doc = thiscomponent
p = doc.currentselection.rangeaddress.sheet
if p = 0 or p = 2 or p =14 or p = 15 or p = 16 or p =17 then
msgbox ("Kunci tidak bisa dibuka disini",0,"Pemberitahuan")
else

l = doc.currentselection.rangeaddress
a = l.sheet
doc.sheets (a).unprotect ("")
end if

end sub

sub tutupkunci
doc = thiscomponent
l = doc.currentselection.rangeaddress
a = l.sheet
doc.sheets (a).protect ("")
end sub


sub sheet1
doc = thiscomponent
p = doc.currentselection.rangeaddress.sheet
print (p)
if p = 0 then
msgbox ("Kunci tidak bisa dibuka disini",0,"Pemberitahuan")
else

end if

end sub



sub insertdatapolisi
doc = thiscomponent
doc.sheets (3).unprotect ("")
Sheet = thiscomponent.sheets(3).getcellrangebyname ("A2:I2")
png = thiscomponent.sheets(3)

png.insertCells(Sheet.rangeaddress, com.sun.star.sheet.CellInsertMode.DOWN)
jenis
c = doc.sheets(1).getcellrangebyname ("E13:M13")
p = doc.sheets(3).getcellrangebyname ("A2:I2")
p.dataarray = c.dataarray


doc.sheets(1).getcellrangebyname ("F13:M13").ClearContents (1 or 2 or 4 or 8 or 16 or 32 or 64)

doc.sheets (3).protect ("")


end sub


sub jenis
doc = thiscomponent
dim P as string
dim PN as string
dim U as string

P = "POLISI"
PN = "PNS"
U  = "UMUM"

jp = doc.currentcontroller.getactivesheet().rangeaddress.sheet

select case jp

case 16
doc.sheets(1).getcellrangebyname ("I13").string = "PNS"

case 15
doc.sheets(1).getcellrangebyname ("I13").string = "POLISI"

case 17
doc.sheets(1).getcellrangebyname ("I13").string = "UMUM"

end select

end sub


