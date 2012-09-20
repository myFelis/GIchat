import socket as sot
from Tkinter import *
from common.constraints import buf_size, all_ip, LOC_ADDR, LOC_PORT_NUM
from common.utils import get_broad_socket, sendmsg

#encoding trauble
reload(sys)
sys.setdefaultencoding('utf-8')

st = get_broad_socket()
st.setsockopt(sot.SOL_SOCKET, sot.SO_REUSEADDR, 1)
st.bind((LOC_ADDR, LOC_PORT_NUM))

msg_configures = None
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

msg_configures = {'user_name': uname, 'user_text': txt}
def _sendmsg(event):
    configs = msg_configures if msg_configures else {}
    sendmsg(event, **configs)

msg.bind('<Return>', _sendmsg)
msg.focus_set()

tk.after(1, func=_proc)
tk.mainloop()
