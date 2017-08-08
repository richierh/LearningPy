#!/usr/bin/python
"""
Berisi tentang proses input data dari GUI ke databases dengan membuat
sebuah class bernama TabelForm
"""

from pony import *
from pony.orm import *
import connection

import pony

class TabelForm(connection.connectdb):
    """
    TabelForm saat database dimasukkan dari GUI ke databases
    """
    def __init__(self,*args,**kwds):
        super(TabelForm,self).__init__()
        self.dataformulir=mylist
        self.data(self.dataformulir)
        return None
  
    def data(self,a):
        return print("data sudah dimasukkan {}".format(self.dataformulir))

mylist=["a","b","c"]
formulir = TabelForm(mylist)
