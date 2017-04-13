# -*- coding: utf-8 -*-
#usr/bin/python
import os,getpass
no = 3
ip ="192.168.1."+str(no)
c = [1,2,3,4,5,6]
#a = list(enumerate(c))
#enumerate(c)
#print a
#print no
#print c[no]

#print os.getenv('USERNAME')
c =  getpass.getuser()
print c

print "ssh",c+"@"+ip


import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

print get_ip()
print "ssh",c+"@"+get_ip()

import os
import socket

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip
print get_lan_ip()


def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if platform.system().lower()=="windows" else "-c 1"
    print platform.system().lower()
    # Ping
    return os.system("ping " + ping_str + " " + host) == 0
print ping("192.168.1.4")

