#!usr/bin/env python
# -*- coding: utf-8 -*-

def insert():
    # Will insert data
    return True
def delete():
    # Will delete data
    return True
def erase():
    # Will erase data
    return True

class Cup:
    def __init__(self):
        self.__color = "hello"
        self._content = None # protected variable

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self.content = None
        
cup = Cup()
cup.__color="eee"
print cup.__color

