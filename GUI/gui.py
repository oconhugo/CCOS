from tkinter import *
import Menu_Frame
from Total_Frame import TotalSection

#This class is in charge of creating the base gui for the cashier.
#Creates left side that will contain the restaurant menu and the right
#Will contain the selected items
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self.left = Frame(self.master, borderwidth=2, relief="solid")
        self.right = Frame(self.master, borderwidth=2, relief="solid")
        self.right.pack(side="right", expand=True, fill="both")

        pad = 3
        self.master.title("Sistema de cobro")
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

        Menu_Frame.MenuSection(self.left, self.right)
        TotalSection(self.right)

    #Function in charge of putting the gui on full screen size
    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

window = Tk()
app = FullScreenApp(window)
window.mainloop()
