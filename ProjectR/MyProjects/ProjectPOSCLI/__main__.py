#/usr/bin/python


def Jawaban():
    if J == 1 :
        print "PENJUALAN"
        pass
    elif J == 2 :
        print "PEMBELIAN"
        pass
    elif J == 3 :
        print "DATA BARANG"
        #Data.Databarang.Databarangku()
        pass
    elif J == 4 :
        print "LAPORAN"
        pass

    else :
        print "Maaf,Pilihan yang anda masukkan tidak ada dalam daftar"



if __name__=="__main__":
    #import Data.Databarang

    try:
        J = input("Silahkan Pilih,\nPilihan Utama\n"
            "1. Penjualan\n2. Pembelian\n3. Data Barang\n4. Laporan\n")
        print "Pilihan yang anda masukkan adalah %s"%J
        Jawaban()
    except (RuntimeError, TypeError, NameError):
        print "Pilihan yang anda masukkan bukan merupakan angka"
