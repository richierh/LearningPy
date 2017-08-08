
from pony.orm import *
import pony.orm

db = Database()


class DataPersonal(db.Entity):
    _resource_ = 'sqlite'
    id = PrimaryKey(int, auto=True)
    id_anggota = Required(int)
    nama = Required(str)
    jenis_kelamin = Optional(str)
    alamat = Optional(str)
    no_telp = Optional(str)


#db.generate_mapping()
