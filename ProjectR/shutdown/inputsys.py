#!/usr/bin/env python
no1="pmc@192.168.1.200"
no2="klien2@192.168.1.2"
no3="klien3@192.168.1.3"
no4="klien4@192.168.1.4"
no5="klien5@192.168.1.5"
no6="klien6@192.168.1.6"
no7="klien7@192.168.1.7"

def myfungsi():
   answer =  raw_input ("Silahkan pilih :\n"
                     " 1.%s\n 2.%s\n 3.%s\n"
                     " 4.%s\n 5.%s\n 6.%s\n 7.%s\n"
                     %(no1,no2,no3,no4,no5,no6,no7))

   if answer.isalpha():
      print "Pilihan Jawaban string"
      exit()

   elif int(answer)<=7 and int(answer)>=1:
      global klien
      print "Pilihan Jawaban cocok "
      klien = eval("no%s"%answer)
      print klien

   else :
       print "Pilihan Jawaban salah"
       exit()
                     
#print answer                  
myfungsi()

