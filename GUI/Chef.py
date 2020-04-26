from tkinter import *
import threading
import socket
import pickle

ORDER_DIC = {}
ORDER_NUM = 0
BUTTON_NUM=1
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting Socket by multithreading")
        server.server_socket(self)

class server(object):
    def __init__(self, master, **kwargs):
        print("3")

    def server_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 3125
        s.bind(('0.0.0.0', port))
        print ('Socket binded to port 3125')
        s.listen(3)
        print ('socket is listening')

        while True:
            c, addr = s.accept()
            message = pickle.loads(c.recv(1024))
            FullScreenApp.set_queue(self, message)



class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        FullScreenApp.master = master
        FullScreenApp.left = Frame(self.master,width=((FullScreenApp.master.winfo_screenwidth())/3), borderwidth=2, relief="solid")
        FullScreenApp.right = Frame(self.master, borderwidth=2, relief="solid")
        FullScreenApp.right.pack(side="right", fill="both",expand=TRUE)
        FullScreenApp.left.pack(side="left", fill="both")

        FullScreenApp.display = Label(self.right, text="")
        FullScreenApp.display.pack()

        pad = 3
        FullScreenApp.master.title("Ordenes")
        FullScreenApp._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

    def createButtons(self):
        global ORDER_NUM
        temp = ORDER_NUM
        children_num=0
        button_order = Button(FullScreenApp.left, text="Order #" + str(temp),
                          height=1, width=60, bg="blue")
        button_order.pack(side="top")
        button_order.config(command=lambda: FullScreenApp.disp_obj(self, button_order['text']))
        for component in FullScreenApp.left.winfo_children():
            children_num=children_num+1
        for component_1 in FullScreenApp.left.winfo_children():
            print(children_num)
            print(FullScreenApp.master.winfo_screenheight())
            print(FullScreenApp.left.winfo_screenheight())
            component_1.config(height=int(27/children_num))

    def disp_obj(self,num):
        global ORDER_DIC
        n = int(num[-1])
        count = len(ORDER_DIC)
        if count>0:
            FullScreenApp.display.config(text=ORDER_DIC[n], width=30, height=10, font=("courier", 17, "bold"))

    def set_queue(self, rx):
        global ORDER_NUM
        global ORDER_DIC
        ORDER_NUM = ORDER_NUM+1
        order_str = ""
        for i in rx:
            for y in i:
                order_str = order_str + "\n" + y
        ORDER_DIC[ORDER_NUM] = order_str
        FullScreenApp.createButtons(self)

thread_server = myThread(1, "Thread-1", 1)
thread_server.start()
window = Tk()
app = FullScreenApp(window)
window.mainloop()
