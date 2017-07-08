import test1

def service_func():
    print 'service func'

if __name__ == '__main__':
    # service.py executed as script
    # do something
    while True:
        service_func()
        test1.some_func()
        raw = input("")
        if raw == 1:
            break
