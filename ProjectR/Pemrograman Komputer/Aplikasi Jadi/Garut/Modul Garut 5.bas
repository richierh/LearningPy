REM  *****  BASIC  *****

Sub Main

End Sub

sub serialkey
	doc = thiscomponent
	c = dateserial (2015,10,30)
	p = doc.sheets(1).getcellrangebyname ("b18").value
	doc.sheets(1).getcellrangebyname ("b20").value = c
	if ( p = c ) then
	print ("komputer mati")
	
		else
		h = inputbox ("Versi trial ini masih bisa dipakai sampai dengan "&c, "HALAMAN PEMBERITAHUAN")
			IF h > "" then
				if h = "1234-ABCD-5678-EFGH" then
				
				msgbox ("Anda Memasukan sandi yang benar",0,"PEMBERITAHUAN")
				
				else 
				
				msgbox ("Anda Memasukan sandi yang salah",0,"PEMBERITAHUAN")
				
				end if	
			else
			exit sub								
			end if
		
	end if
	
	
end sub

sub j
ThisComponent.close(True)
end sub
