class Goto(Exception):
 pass


def okay():
 try:
    foo = "bar"
    if foo == "bar":
        raise Goto
    print ("foo is not bar")
 except Goto:
    print ("foo is bar")

okay()
