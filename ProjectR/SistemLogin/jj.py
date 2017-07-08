import datetime
import time

pengirim = "Saya"
penerima = "Kalian"
tanggal = datetime.date
waktu = datetime.datetime.now().strftime("%H:%M:%S")
print "NGACA DONG"
print "-" * 70
print "Tanggal: " + str(tanggal.today())
print "\n"
print "Waktu : " +str(waktu)
print "\n"
print "Dari: " + pengirim
print "\nUntuk: " + penerima
print "\n"

isi = """Sebelum Kalian Menilai Saya Ada Baiknya Kalian Berkaca Terlebih Dahulu \nUdah Bener Apa Belum Hidup Lo Yang Kemarin, Sekarang, Atau nanti. \nJangan Bisanya Ngomentarin Hidup Gw Doang."""

print isi

print "-" * 70
