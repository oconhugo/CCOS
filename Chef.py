from tkinter import *
import threading
import socket
import pickle
from queue import Queue

ORDER_QUEUE = Queue()
ORDER_NUM = 0
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
        FullScreenApp.left = Frame(self.master, borderwidth=2, relief="solid")
        FullScreenApp.right = Frame(self.master, borderwidth=2, relief="solid")
        FullScreenApp.right.pack(side="right", expand=True, fill="both")
        FullScreenApp.left.pack(side="left", expand=True, fill="both")

        FullScreenApp.display = Label(self.right, text="k")
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
        while not input.empty():
            FullScreenApp.display.config(text=str(input.get()))

    def set_queue(self, rx):
        global ORDER_QUEUE
        ORDER_QUEUE.put(rx)
        FullScreenApp.show_order(self,ORDER_QUEUE)
        print('queue size' + str(ORDER_QUEUE.qsize()))

thread_server = myThread(1, "Thread-1", 1)
thread_server.start()
window = Tk()
app = FullScreenApp(window)
window.mainloop()
