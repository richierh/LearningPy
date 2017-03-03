#/usr/bin/python#
#This is if condition and have the function similar to goto inside of the code#
def kondisi1():
    print "Yah itu dia yang saya maksud\n"
def kondisi2():
    print "Bukan itu jawaban yang cerdas\n"
password = "komputer"
while True:
 text = raw_input("Silahkan masukkan password yang benar?\n")
 if text == password :
  print ("Password anda sudah benar '"+password+"', Selamat\n")
  break
 else:
  print ("Password yang benar bukan '"+text+"',Silahkan dicoba kembali\n")

nama_kamu = "saya"
while True:
 textnama = raw_input ("Nama kamu siapa?\n")
 if nama_kamu==textnama:
    kondisi1()
    break
 else:
    kondisi2()
