def add_user(store):
    user = raw_input('Create Username: ')
    password = raw_input('Create Password: ')
    if user in store:
        print "That user already exsist"
        return False
    else:
        store[user] = password
        return True

# and call this 10 times for example...
global_store = dict()
for i in range(10):
    add_user(global_store)