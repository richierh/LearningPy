# -*- coding: utf-8 -*-


class databarang(object):
    global inputdatabarang
    global hasil
    def __init__(self):
        super(databarang, self).__init__()
        inputdatabarang(self)

    def inputdatabarang(self):
        nomor_brg = raw_input("Silahkan masukkan nomor barang\n")

        nama_brg = raw_input("Silahkan masukkan nama barang\n")
        besaran_brg =  raw_input ("Silahkan masukkan jenis Besaran\n"
                        "(kg,lembar,meter,dsb\n")
        if besaran_brg in ["kg","lembar","meter"]: # "kg" or besaran_brg == "lembar" or besaran_brg ==  "meter":
            pass
        else :
            besaran_brg = "tidak ada"
            pass

        Jmlsatuan_brg = raw_input("Silahkan masukkan jumlah barang yang dibeli\n")
        self.nomor_brg=nomor_brg
        self.nama_brg = nama_brg
        self.besaran_brg=besaran_brg
        self.Jmlsatuan_brg =  Jmlsatuan_brg
        hasil(self)

    def hasil(self):

        print "%s  %s  %s  %s"%(self.nomor_brg,self.nama_brg,self.Jmlsatuan_brg,self.besaran_brg)
        pass

if __name__=="__main__":
    databarang()

 
