import socket as sot
from common.constraints import LOC_PORT_NUM, LOC_ADDR, buf_size
from common.utils import get_broad_socket


st = get_broad_socket()
st.setsockopt(sot.SOL_SOCKET, sot.SO_REUSEADDR, 1)
st.bind((LOC_ADDR, LOC_PORT_NUM))
while True:
    msg = st.recv(buf_size)
    print msg
