import socket as sot


def get_broad_socket():
    st = sot.socket(sot.AF_INET, sot.SOCK_DGRAM)
    st.setsockopt(sot.SOL_SOCKET, sot.SO_BROADCAST, 1)
    return st
