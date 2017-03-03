# /usr/bin/env python
# This is an example to get connected to other clients (local network)
# by using Paramiko package in combination with my own code
# And don't forget... Please correct me if I am wrong (Richie)

class mainclass(object):
    print ("This is the mainclass running")

    def __init__(self,no_client):
        self.no_client = no_client
        self.accesclient()

    def accesclient(self):
        self.id = "klien%d@192.168.1.%d" % (self.no_client, self.no_client)
        self.sshprocess()

    def sshprocess(self):
        # from this , I will get the paramiko package
        # I haven't finished my code though --cheers
        import paramiko
        print ("Now entering sshprocess")
        pass

if __name__ == "__main__":
    print ("Please Choose your client to get connected?")
    client = 6 #--> it will use raw_input or just input for inputing by the user
    app = mainclass(client)
    print app.id
