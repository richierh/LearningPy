REM  *****  BASIC  *****

Sub Main
sTitle = "Tes"

print sTitle

End Sub

    Function getFolder(sTitle AS String, optional sInitDir) AS String
       oPicker = CreateUnoService("com.sun.star.ui.dialogs.FolderPicker")
       oPicker.setTitle(sTitle)
       if not ismissing(sInitDir) then oPicker.setDisplayDirectory(sInitDir)
       if oPicker.execute() then getFolder = oPicker.getDirectory()
    End Function

