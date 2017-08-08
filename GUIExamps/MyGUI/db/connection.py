from pony.orm import *
from ormpony import *

#db = Database()
db.bind(provider='sqlite', filename='mydatabase.sqlite', create_db=True)
show(DataPersonal)
sql_debug(True)
#db.generate_mapping(False)
db.generate_mapping(create_tables=True)

