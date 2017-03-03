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