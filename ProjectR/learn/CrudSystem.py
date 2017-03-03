# /usr/bin/env python

def masukandata():
    print ("Silahkan masukkan nomor ID")
    idmu = raw_input("")
    print ("Silahkan masukkan nama anda?")
    namamu = raw_input("")
    print ("Silahkan masukkan data tanggal lahir anda dd/mm/yyyy?")
    tgllahirmu = raw_input("")
    print ("Silahkan masukkan data kota tempat tinggal")
    tempattinggal = raw_input("")
    return idmu,namamu,tgllahirmu, tempattinggal


def data():
    idmu,namamu,tgllahirmu,tempattinggal=masukandata()
    print "|ID         |Nama               |Tgl Lahir      |Kota Tempat Tinggal         |"
    print " ",idmu,"         ",namamu,"                 ",tgllahirmu,"            ",tempattinggal
    #print namamu
    #print tgllahirmu
    #print tempattinggal

def query():
    print ("Silahkan nama yang ingin di cari")
    qnama = raw_input("")



J = masukandata()
print J
