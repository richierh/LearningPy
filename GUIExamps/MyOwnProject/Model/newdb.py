# -*- coding: utf-8 -*-

from pony.orm import *

data = Database ("sqlite","database.sqlite",create_db=True)