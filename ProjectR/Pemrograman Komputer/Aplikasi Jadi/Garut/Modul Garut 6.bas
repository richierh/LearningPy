   Sub Find
        
    dim A as string
    oDoc = ThisComponent
    L = oDoc.sheets(1).getcellrangebyname ("j2")
    sAns = L.string
    If sAns = "" then End 'Blank entry or Cancel clicked.

    oSheet = oDoc.sheets(3).getcellrangebyname ("f2:f1500")'Get active sheet.
    FandR = oSheet.createSearchDescriptor 'Set up find and replace.
    FandR.setSearchString(sAns)
	FandR.setSearchString(sAns)
    'FandR.SearchWords = true 'Entire cell must match.
        oCell = oSheet.findfirst(FandR)
		P = oCell.celladdress.row
    
    
    print (p)
    End Sub
    

    Sub StartDialog2()
    BasicLibraries.LoadLibrary("Standard")
	Dlg = CreateUnoDialog(DialogLibraries.Standard.Dialog1)
    Dlg.Execute()
	End Sub
    
    Dim Dlg As Object
 
 sub closex
DialogLibraries.LoadLibrary("Standard")
Dlg = CreateUnoDialog(DialogLibraries.Standard.Dialog1)
Select Case Dlg.Execute() 
Case 1
Case 0 
End Select
end sub  
