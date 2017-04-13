REM  *****  BASIC  *****

Sub Main

End Sub

REM  *****  BASIC  *****

Sub awalbuka


End Sub

sub pemberitahuan
msgbox ("Software ini masih dalam versi trial dan akan berakhir pada tanggal 30 Januari 2016",0,"Pemberitahuan")

end sub


sub closel

doc = thiscomponent
dateexpired = dateserial (2016,01,30)
datenow = doc.sheets(1).getcellrangebyname("B31").value
doc.sheets(1).getcellrangebyname("B32").value = dateexpired

if datenow >= dateexpired then

doc.close (true)
doc.terminate

else 

exit sub

end if
end sub

Sub sambutan

MsgBox "Aplikasi Multi Usaha.IstCell" ,0,"PMC Software"


end sub


Sub tutupsemuatoolbar3
bukasheet
bukacolumnrow
bukascrollbar
bukatoolbar
bukaformula
bukastatusbar
end sub

Sub tutupsemuatoolbar
tutupsheet
tutupcolumnrow
tutupscrollbar
tutupformula
tutupstatusbar
Toolbarshow
tutuptoolbar
end sub


Sub tutupsemuatoolbar2

tutupsheet
tutupcolumnrow
tutupscrollbar
tutupformula
tutupstatusbar
Toolbarshow
tutuptoolbar
tampilan
data3
tampilan

end sub

rem //
sub tampilan

doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(0)
seleksi.select (menuju)

end sub

sub data3

doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(3)
seleksi.select (menuju)

end sub

rem -----------------------
sub bukasheet
doc = thiscomponent
l =  thiscomponent.currentcontroller
l.sheettabs = true

end sub
rem -----------------------

sub tutupsheet
doc = thiscomponent
l =  thiscomponent.currentcontroller
l.sheettabs = false

end sub


sub bukacolumnrow
doc = thiscomponent
l =  thiscomponent.currentcontroller
l.columnrowheaders = true
end sub

rem -----------------------

sub tutupcolumnrow
doc = thiscomponent
l =  thiscomponent.currentcontroller
l.columnrowheaders = false
end sub


sub bukascrollbar
	controller = thisComponent.currentController
	controller.horizontalscrollbar = true
	controller.verticalscrollbar = true
end sub

rem -----------------------

sub tutupscrollbar
	controller = thisComponent.currentController
	controller.horizontalscrollbar = false
	controller.verticalscrollbar = false
end sub

rem -----------------------
sub bukagrid

	controller = ThisComponent.CurrentController
    controller.ShowGrid = true

end sub

rem -----------------------

sub tutupgrid

	controller = ThisComponent.CurrentController
    controller.ShowGrid = false

end sub

rem------------
sub bukasimbol
	controller = ThisComponent.CurrentController
    controller.outlinesymbols = true
end sub

rem --------------------------------------
sub tutupsimbol
	controller = ThisComponent.CurrentController
    controller.outlinesymbols = false
end sub


sub bukatoolbar

thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/alignmentbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/arrowshapes")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/basicshapes")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/calloutshapes")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/colorbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/drawbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/drawobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/extrusionobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/fontworkobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/fontworkshapetypes")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/formatobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/formcontrols")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/formdesign")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/formsfilterbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/formsnavigationbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/formsobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/formtextobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/fullscreenbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/graphicobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/insertbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/insertcellsbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/insertobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/mediaobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/moreformcontrols") 
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/previewbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/standardbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/starshapes")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/symbolshapes")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/textobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/toolbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/toolbar/viewerbar")
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/menubar/menubar" )
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/menubar/viewbar" )
thiscomponent.currentcontroller.frame.layoutmanager.showelement ("private:resource/menubar/scrollbar" )

end sub

sub tutuptoolbar

thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/alignmentbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/arrowshapes")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/basicshapes")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/calloutshapes")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/colorbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/drawbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/drawobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/extrusionobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/fontworkobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/fontworkshapetypes")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/formatobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/formcontrols")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/formdesign")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/formsfilterbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/formsnavigationbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/formsobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/formtextobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/fullscreenbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/graphicobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/insertbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/insertcellsbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/insertobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/mediaobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/moreformcontrols") 
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/previewbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/standardbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/starshapes")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/symbolshapes")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/textobjectbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/toolbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/toolbar/viewerbar")
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/menubar/menubar" )
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/menubar/viewbar" )
thiscomponent.currentcontroller.frame.layoutmanager.hideelement ("private:resource/menubar/scrollbar" )

end sub

rem ---------------- hide formula bar
Sub bukaformula (Optional showBar As Boolean)
    Dim oDoc As Object
    Dim oDisp As Object
    Dim args(0) As new com.sun.star.beans.PropertyValue

    If IsMissing(showBar) Then showBar = true
       args(0).Name = "InputLineVisible"
       args(0).Value = ShowBar
       oDoc = ThisComponent.CurrentController.Frame
       oDisp = createUnoService("com.sun.star.frame.DispatchHelper")
       oDisp.executeDispatch(oDoc, ".uno:InputLineVisible", "", 0, args())
       
end sub
Sub tutupformula (Optional showBar As Boolean)
    Dim oDoc As Object
    Dim oDisp As Object
    Dim args(0) As new com.sun.star.beans.PropertyValue

    If IsMissing(showBar) Then showBar = false
       args(0).Name = "InputLineVisible"
       args(0).Value = ShowBar
       oDoc = ThisComponent.CurrentController.Frame
       oDisp = createUnoService("com.sun.star.frame.DispatchHelper")
       oDisp.executeDispatch(oDoc, ".uno:InputLineVisible", "", 0, args())
       
end sub

Sub bukastatusbar (Optional showBar As Boolean)
    Dim oDoc As Object
    Dim oDisp As Object
    Dim args(0) As new com.sun.star.beans.PropertyValue

    If IsMissing(showBar) Then showBar = true
       args(0).Name = "StatusBarVisible"
       args(0).Value = ShowBar
       oDoc = ThisComponent.CurrentController.Frame
       oDisp = createUnoService("com.sun.star.frame.DispatchHelper")
       oDisp.executeDispatch(oDoc, ".uno:StatusBarVisible", "", 0, args())
       
end sub

Sub tutupstatusbar (Optional showBar As Boolean)
    Dim oDoc As Object
    Dim oDisp As Object
    Dim args(0) As new com.sun.star.beans.PropertyValue

    If IsMissing(showBar) Then showBar = false
       args(0).Name = "StatusBarVisible"
       args(0).Value = ShowBar
       oDoc = ThisComponent.CurrentController.Frame
       oDisp = createUnoService("com.sun.star.frame.DispatchHelper")
       oDisp.executeDispatch(oDoc, ".uno:StatusBarVisible", "", 0, args())
       
end sub


Sub Toolbarshow
 Dim L as string
 L = "KembaliTampilanUtama"
  oDoc = ThisComponent
  sResId = FindToolbar(oDoc, L)
  if not isnull(sResId) then
    oManager = oDoc.getCurrentController().getFrame().LayoutManager
    oManager.createElement(sResId)
    oManager.ShowElement(sResId)
  end if
End Sub

Sub Toolbarhide
 Dim L as string
 L = "KembaliTampilanUtama"
  oDoc = ThisComponent
  sResId = FindToolbar(oDoc, L)
  if not isnull(sResId) then
    oManager = oDoc.getCurrentController().getFrame().LayoutManager
    oManager.createElement(sResId)
    oManager.hideElement(sResId)
  end if
End Sub
rem --------
Function FindToolbar(oDoc, sName As String)
  oManager = oDoc.getUIConfigurationManager()
  aElements = oManager.getUIElementsInfo(_
       com.sun.star.ui.UIElementType.TOOLBAR)
  itemset = nothing
  for i = 0 to ubound(aElements) step 1
    a = aElements(i)
    if GetPropertyValueByName(a, "UIName") = sName then
      itemset = a
      exit for
    end if
  next
  if not isnull(itemset) then
    FindToolbar = GetPropertyValueByName(itemset, "ResourceURL")
  else
    FindToolbar = nothing
  end if
End Function

Function GetPropertyValueByName(aElements, sName) As Variant
  found = nothing
  for i = 0 to ubound(aElements) step 1
    if aElements(i).Name = sName then
      found = aElements(i).Value
    end if
  next
  GetPropertyValueByName = found
End Function


Sub tutupmanagerlayout( )
    doc = ThisComponent
    frame = doc.CurrentController.Frame
    lmgr = frame.LayoutManager
    lmgr.setvisible (true)
End Sub

Sub toolbarshow1
oFrame = ThisComponent.CurrentController.Frame
    layout = oFrame.LayoutManager
    sUrl1="private:resource/toolbar/KembaliTampilanUtama"

    layout.hideElement (sUrl1)

    
End Sub
