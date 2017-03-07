#!usr/bin/python

# Now I am going to write a simple code to connect into sql file.


import sqlite3


class csql():
	def __init__(self,parent):
		self.koneksi = sqlite3.connect("test.db")
		self.koneksi
		self.go()
		print "Koneksi berhasil"
	def go(self):
		self.koneksi.cursor()



if __name__=="__main__":
	fconnect = csql(None)
	

