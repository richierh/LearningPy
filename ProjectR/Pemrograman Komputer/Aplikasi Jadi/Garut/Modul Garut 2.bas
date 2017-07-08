REM  *****  BASIC  *****

Sub Main

End Sub

sub tampilan

doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(0)
seleksi.setactivesheet (menuju)

end sub

sub datapu

doc = thiscomponent
rem ----------------------------------------------------------------------
gotoprint=doc.sheets(3)
gotoprint2 = doc.currentcontroller

gotoprint2.setactivesheet(gotoprint)

end sub


sub menujukedatapasien

doc = thiscomponent
rem ----------------------------------------------------------------------
gotoprint=doc.sheets(2)
gotoprint2 = doc.currentcontroller

gotoprint2.setactivesheet(gotoprint)

end sub

sub menujukedatakunjunganpasien

doc = thiscomponent
rem ----------------------------------------------------------------------
gotoprint=doc.sheets(4)
gotoprint2 = doc.currentcontroller

gotoprint2.setactivesheet(gotoprint)

end sub

sub rekaphasil
doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(14)
seleksi.setactivesheet (menuju)

end sub

sub inputpolisi
doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(15)
seleksi.setactivesheet (menuju)

end sub

sub Inputpns
doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(16)
seleksi.setactivesheet (menuju)

end sub
sub inputumum
doc=thiscomponent
seleksi = doc.currentcontroller
menuju = doc.sheets(17)
seleksi.setactivesheet (menuju)

end sub



