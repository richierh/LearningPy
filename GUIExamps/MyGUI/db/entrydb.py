#!/usr/bin/python

from pony import *
from pony.orm import *

import pony

class TabelForm():
    """
    TabelForm saat database dimasukkan dari GUI ke database
    """
    def __init__(self,dataformulir):
        self.dataformulir=dataformulir
        self.data(self.dataformulir)
        return None
  
    def data(self,a):
        return print("data sudah dimasukkan {}".format(self.dataformulir))

mylist=["a","b","c"]
formulir = TabelForm(mylist)
