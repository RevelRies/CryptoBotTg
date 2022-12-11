import pony
from pony.orm import *
import models

db = Database()

class User(db.Entity):
    user_id = Required(str)
    nick = Required(str)
    age = Required(int)
    wallets = Set('Wallet')


class Wallet(db.Entity):
    address = Required(str)
    private_key = Required(str)
    owner = Required(User)

try:
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
except Exception as e:
    print(e)

# set_sql_debug(True)
#
# db.generate_mapping(create_tables=True)
#
# u1 = User(nick='John', user_id="20", age=25)
# u2 = User(nick='Mary', user_id="22", age=26)
# u3 = User(nick='Bob', user_id="30", age=35)
# w1 = Wallet(address='address1', private_key='private_key1', owner=u2)
# w2 = Wallet(address='address2', private_key='private_key2', owner=u3)