save = []
status = []
user = {
    #status, username, password
    "admin":["admin", "admin"],
    "user":[['hello', 'world'],
            ['open', 'close']]
    }
menu = {'out':'for logout',
        'switch':'for change account',
        'menu':'for more menu'
        }

def cekstatus():
    global status
    if status[0] == 'admin':
        print('^^ you are admin, type "cp" for control panel, "help" for view all command.')
        asadm()
    else:
        print('^^ welcome, type "help" for view all command.')
        asusr()

def asadm():
    while True:
        x = input("> ").lower()
        if x == "cp":
            cp()
        elif x == "out":
            print('_thank_you')
            break

def asusr():
    while True:
        x = input("> ").lower()
        if x == "out":
            print('_thank_you')
            break
        elif x == 'help':
            for key in menu:
                print(key,'\t', menu[key])
            continue
        break

def cp():
    global user
    while True:
        print('1. view all user')
        print('2. set user as admin')
        print('3. delete user')
        print('4. change username and password')
        print('5. close')
        x = input("> ")
        if x == "1":
            for u in range(len(user['user'])):
                print(u+1, user['user'][u][0])
            print()
        elif x == "2":
            print('select user :')
            for u in range(len(user['user'])):
                print(u+1, user['user'][u][0], "code : ", u)
                print('type the code to promote as admin')
                op = int(input("> "))
                for h in range(len(user['user'])):
                    if op == h:
                        user['admin'].append(user['user'][h])
                        print('now',user['admin'][int(len(user['admin']) - 1)][0], "is an admin")
                        user['user'].remove(user['user'][h])
                        print("admin list updated")
                        print(user['admin'][0::][0])
def login():
    print('1. login')
    print('2. create new user')
    while True:
        try:
            sel = int(input("> "))
            if sel == 1:
                while True:
                    x = input('username: ').lower()
                    y = input('password: ').lower()
                    if x in user['admin']:
                        if x in user['admin'][0]:
                            if y in user['admin'][1]:
                                print('_loged_in_as_admin')
                                status.append('admin')
                                status.append(x)
                                cekstatus()
                                break
                            else:
                                print('_WrongPassword')
                                continue
                        else:
                            print('_WrongUsername')
                            continue
                    else:
                        for i in range(len(user['user'])):
                            if x in user['user'][i][0]:
                                if y in user['user'][i][1]:
                                    print('_loged_in_as_user')
                                    status.append('user')
                                    status.append(x)
                                    cekstatus()
                                    break
                                elif y not in user['user'][i][1]:
                                    print('_WrongPassword')
                                    continue
                            elif x not in user['user'][i][0]:
                                print('_WrongUsername')
                                continue
                        continue
                    break
            if sel == 2:
                while True:
                    x = input('new username: ')
                    for u in range(len(user['user'])):
                        if x in user['user'][u][0]:
                            print('_User_is_Already_Exist')
                            continue
                    break
                while True:
                    y = input('new password: ')
                    z = input('re-type new password: ')
                    if z != y:
                        print('_PasswordIncorect')
                        continue
                    break
                user['user'].append([x, y])
                print(user)
                continue
        except ValueError:
            print('_type_1_or_2')
            login()
        break

login()
