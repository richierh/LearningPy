REM  *****  BASIC  *****


sub Main
rem ----------------------------------------------------------------------
rem define variables
dim document   as object
dim dispatcher as object
rem ----------------------------------------------------------------------
rem get access to the document
document   = ThisComponent.CurrentController.Frame
dispatcher = createUnoService("com.sun.star.frame.DispatchHelper")

rem ----------------------------------------------------------------------
dispatcher.executeDispatch(document, ".uno:Print", "", 0, Array())


end sub


    Sub PrintShets
    aSheets = Array(1, 3)                   '... , .5, 6,...etc
       For i=0 to uBound(aSheets)
          JumpToSheet(aSheets(i))
          PrintActiveSheet()      'it is the your print routine
       next i
    end sub

    sub JumpToSheet(SheetNumber)

    ' Recorded by MacroRecorder, but edited (modified) manually.

    rem ----------------------------------------------------------------------
    rem define variables
    dim document   as object
    dim dispatcher as object
    rem ----------------------------------------------------------------------
    rem get access to the document
    document   = ThisComponent.CurrentController.Frame
    dispatcher = createUnoService("com.sun.star.frame.DispatchHelper")

    rem ----------------------------------------------------------------------
    dim args1(0) as new com.sun.star.beans.PropertyValue
    args1(0).Name = "Nr"
    args1(0).Value = SheetNumber    ' It is the modified parameter

    dispatcher.executeDispatch(document, ".uno:JumpToTable", "", 0, args1())


    end sub
    
sub printRange
rem ----------------------------------------------------------------------
rem define variables
dim document   as object
dim dispatcher as object
rem ----------------------------------------------------------------------
rem get access to the document
document   = ThisComponent.CurrentController.Frame
dispatcher = createUnoService("com.sun.star.frame.DispatchHelper")

rem ----------------------------------------------------------------------
rem this defines the range to be printed.  If the desired range is not a contiguous block, something
rem more complicated would be needed
dim args1(0) as new com.sun.star.beans.PropertyValue
args1(0).Name = "ToPoint"
args1(0).Value = "$B$2:$D$6"

dispatcher.executeDispatch(document, ".uno:GoToCell", "", 0, args1())

rem ----------------------------------------------------------------------
rem define the parameters for the export/print to PDF – including filename for output.
dim args2(2) as new com.sun.star.beans.PropertyValue
args2(0).Name = "URL"
args2(0).Value = "file:////home/pmc/Documents/pdfPrint_selectedCellsCalcSheet_byMacro.pdf"
args2(1).Name = "FilterName"
args2(1).Value = "calc_pdf_Export"
args2(2).Name = "FilterData"
args2(2).Value = Array(Array("UseLosslessCompression",0,false,com.sun.star.beans.PropertyState.DIRECT_VALUE),,Array("SignatureCertificate",0,,com.sun.star.beans.PropertyState.DIRECT_VALUE))

dispatcher.executeDispatch(document, ".uno:ExportToPDF", "", 0, args2())
rem    enter code hersub printRange
rem ----------------------------------------------------------------------
rem define ...
end sub




    sub printing

    DIM parametry_drukowania(1) AS NEW com.sun.star.beans.PropertyValue
        parametry_drukowania(0).Name = "CopyCount"
        parametry_drukowania(0).Value = 1
        parametry_drukowania(1).Name = "Pages"
        parametry_drukowania(1).Value = "1"
        ThisComponent.CurrentController.ActiveSheet = ThisComponent.Sheets.getByName("sheet2")

       thisComponent.Print(parametry_drukowania)

    MsgBox "Sheet have been printed with 1 copy."     

    end sub


sub setprintarea
doc = thiscomponent

l = doc.sheets(1).getcellrangebyname("G9").value
rem ----------------------------------------------------------------------
rem define variables
dim document   as object
dim dispatcher as object
rem ----------------------------------------------------------------------
rem get access to the document
document   = ThisComponent.CurrentController.Frame
dispatcher = createUnoService("com.sun.star.frame.DispatchHelper")

rem ----------------------------------------------------------------------
dim args1(0) as new com.sun.star.beans.PropertyValue
args1(0).Name = "ToPoint"
args1(0).Value = "$A$1:$E$"&l

dispatcher.executeDispatch(document, ".uno:GoToCell", "", 0, args1())

rem ----------------------------------------------------------------------
dispatcher.executeDispatch(document, ".uno:DefinePrintArea", "", 0, Array())


end sub

