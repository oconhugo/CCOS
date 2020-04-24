from tkinter import *
import threading
from server import server

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        server.server_socket(self)
        print("Starting " + self.name)
        print("Exiting " + self.name)

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self.left = Frame(self.master, borderwidth=2, relief="solid")
        self.right = Frame(self.master, borderwidth=2, relief="solid")
        self.right.pack(side="right", expand=True, fill="both")
        self.left.pack(side="left", expand=True, fill="both")

        pad = 3
        self.master.title("Ordenes")
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

thread_server = myThread(1, "Thread-1", 1)
thread_server.start()
window = Tk()
app = FullScreenApp(window)
window.mainloop()
