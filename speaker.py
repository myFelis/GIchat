import socket as sot
from common.constraints import LOC_PORT_NUM, all_addr
from common.utils import get_broad_socket


st = get_broad_socket()
while True:
    st.sendto('BROADCAST', (all_addr, LOC_PORT_NUM))
