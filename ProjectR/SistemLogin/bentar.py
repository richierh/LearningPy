

def hello(name=''):
    if name == '':
        message = u"Hello, World!"
    else:
        message = u"Hello, {}!".format(name)
    print message
    return message

hello()
