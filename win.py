import socket as sot
from Tkinter import *
from common.constraints import buf_size, all_addr, LOC_ADDR, LOC_PORT_NUM
from common.utils import get_broad_socket

#kirill trauble
reload(sys)
sys.setdefaultencoding('utf-8')

st = get_broad_socket()
st.setsockopt(sot.SOL_SOCKET, sot.SO_REUSEADDR, 1)
st.bind((LOC_ADDR, LOC_PORT_NUM))

sock = get_broad_socket()

tk = Tk()
hist = Text(tk)

def _proc():
    hist.see(END)
    st.setblocking(False)
    try:
        message = st.recv(buf_size)
        hist.insert(END, message+'\n')
    except:
        tk.after(1,_proc)
        return
    tk.after(1,_proc)
    return

txt, uname = StringVar(), StringVar()
txt.set('text')
uname.set('Test UserName')
tk.title('GIchat')
h, w = 600, 450
tk.geometry('%sx%s' % (h,w))

username = Entry(tk, textvariable=uname)
msg = Entry(tk, textvariable=txt)
hist.pack(side='top', fill='both', expand='true')
username.pack(side='bottom', fill='x', expand='true')
msg.pack(side='bottom', fill='x', expand='true')

def _sendproc(event):
    sock.sendto(':'.join([uname.get(),txt.get()]), (all_addr, LOC_PORT_NUM))
    txt.set('')

msg.bind('<Return>', _sendproc)
msg.focus_set()

tk.after(1, func=_proc)
tk.mainloop()
