import socket as sot
from Tkinter import StringVar
from common.constraints import all_ip, LOC_PORT_NUM


def get_broad_socket():
    st = sot.socket(sot.AF_INET, sot.SOCK_DGRAM)
    st.setsockopt(sot.SOL_SOCKET, sot.SO_BROADCAST, 1)
    return st

def sendmsg(event, **kwargs):
    if kwargs.has_key('user_name'):
        uname = kwargs.get('user_name')
    else:
        uname = StringVar()
        uname.set('Anonymous')
    if kwargs.has_key('user_text'):
        txt = kwargs.get('user_text')
    else:
        txt = StringVar()
        txt.set('')
    if kwargs.has_key('socket'):
        sock = kwargs.get('socket')
    else:
        sock = get_broad_socket()
    if kwargs.has_key('ip'):
        address = kwargs.get('ip')
    else:
        address = all_ip
    if kwargs.has_key('port_number'):
        port_num = kwargs.get('port_number')
    else:
        port_num = LOC_PORT_NUM
    s = ':'.join([uname.get(),txt.get()])
    sock.sendto(s, (address, port_num))
    txt.set('')