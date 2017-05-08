#!/usr/bin/python


Daftar_barang = {"Sikat gigi":"Rp 2000","Chicki":"Rp 3500"}

entri = "Silahkan masukkan harga produk"
print list(Daftar_barang.iteritems())
print Daftar_barang.iteritems
print Daftar_barang.items()


print entri
inputharga = raw_input()

print Daftar_barang.get(inputharga)
                 
                 
