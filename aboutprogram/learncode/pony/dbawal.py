# /usr/bin/env python

from pony.orm import*

db =  Database()

class Orang(db.Entity):
    nama  = Required(str)
    usia  = Required(int)
    mobil = Set('Mobil')

class Mobil(db.Entity):
    produk  = Required(str)
    model   = Required(str)
    pemilik = Required(Orang)
show(Orang)
