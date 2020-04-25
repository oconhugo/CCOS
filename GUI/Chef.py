from tkinter import *
import threading
import socket
import pickle
from queue import Queue

ORDER_QUEUE = Queue()
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

    def show_order(self, input):
        children_num=0
        global ORDER_QUEUE
        while not input.empty():
            temp_obj = input.get()
            button_order = Button(FullScreenApp.left, text="Order #" + str(ORDER_NUM),
                                  command=lambda: FullScreenApp.disp_obj(self, temp_obj),
                                  height=1, width=60, bg="blue")
            button_order.pack(side="top")
        for component in FullScreenApp.left.winfo_children():
            children_num=children_num+1
        for component_1 in FullScreenApp.left.winfo_children():
            print(children_num)
            print(FullScreenApp.master.winfo_screenheight())
            print(FullScreenApp.left.winfo_screenheight())
            component_1.config(height=int(27/children_num))

    def disp_obj(self,inp_obj):
        order_str= ""
        while len(inp_obj)>0:
            temp_object = inp_obj.pop()
            print(str(temp_object))
            for i in temp_object:
                order_str = order_str + "\n" + i
            FullScreenApp.display.config(text=str(order_str))

    def set_queue(self, rx):
        global ORDER_QUEUE
        global ORDER_NUM
        ORDER_NUM = ORDER_NUM+1
        ORDER_QUEUE.put(rx)
        FullScreenApp.show_order(self,ORDER_QUEUE)
        print('queue size' + str(ORDER_QUEUE.qsize()))

thread_server = myThread(1, "Thread-1", 1)
thread_server.start()
window = Tk()
app = FullScreenApp(window)
window.mainloop()
