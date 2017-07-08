#!usr/bin/env python
from pony.orm import *


db = Database()


class DataBarang(db.Entity):
    id = PrimaryKey(int, column='ID', auto=True)
    lkodebrg = Required(int, column="KODE BARANG")
    lnamabrg = Required(str, column="NAMA BARANG")
    lsatuan = Required(str, column='SATUAN')
    ljumlah = Required(int, column='JUMLAH')
    lhargajual = Required(int, column="HARGA JUAL")
    lhargabeli = Required(int, column="HARGA BELI")
    lstok = Required(int, column='STOK')
    data_penjualans = Set('DataPenjualan')


class DataPenjualan(db.Entity):
    idpenj = PrimaryKey(int, column="ID PENJUALAN", auto=True)
    kodepenj = Required(str, column="KODE PENJUALAN")
    penjbrg = Required(str, column="PENJUALAN BARANG")
    penjsatuan = Required(str, column='SATUAN')
    penjkuantiti = Required(int, column='KUANTITI')
    penjhrgjual = Required(int, column="HARGA JUAL")
    penjtotal = Required(int, column="TOTAL HARGA")
    data_barangs = Set(DataBarang)
    penjdiskon = Optional(int, column='DISKON')


db.bind("sqlite", "database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)