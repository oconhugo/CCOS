from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
import Menu_Frame
from client import client

#Display the total and buttons
class TotalSection(object):
    def __init__(self, right):
        label4 = Label(right, text="Articulos Seleccionados", width=30, height=2, font=("courier", 17, "bold"))
        label5 = Label(right, text="Articulo          Precio", width=30, height=2, font=("courier", 10, "bold"))
        label4.pack()
        label5.pack()
        TotalSection.createScrolling(self, right)
        box = Frame(right, borderwidth=2)
        total_label = Label(box, text="Total=   " + str(0), width=30, height=2, font=("ariel", 17, "bold"))
        box.pack(side="bottom", expand=True, fill="both", padx=10, pady=10)
        nota = self.newNota(box)
        continuar = Button(box, text="Continuar",height = 4, width=25, bg="lime green", padx=10, pady=10, command= lambda: self.continuar(nota))
        cancelar = Button(box, text="cancelar",height = 4, width=25, bg="fireBrick2", padx=10, pady=10, command= lambda: self.delete())
        continuar.pack(side = "left")
        cancelar.pack( side = "left")

    def createScrolling(self, right):
        container = ttk.Frame(right)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        TotalSection.scrollable_frame = ttk.Frame(canvas)
        TotalSection.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=TotalSection.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    #Regresa la nota para el taquero
    def newNota(self, box):
        F = Frame(box)
        F.pack()
        L1 = Label(F, text="Nota para el taquero",font=("arial", 10, "bold"))
        L1.pack(side=LEFT)
        E1 = Text(F, bd=3, height=2, width=20)
        E1.pack(side=RIGHT)
        return E1

    #Manda el JSON hacia la otra interfase
    def continuar(self, nota):
        global ORDER
        #send order just when ver total is pressed
        if(Menu_Frame.DISM==0):
            messagebox.showinfo("Order", "Presione Ver total primero")
        else:
            global ORDER
            if len(ORDER)>0:
                ORDER.append({"Nota":nota.get("1.0", "end-1c")})
                client.client_socket(self, ORDER)
                messagebox.showinfo("Order", "Order sended successfully")
            else:
                messagebox.showinfo("Order", "No items selected")
            self.delete(nota)

    #Reset the values of the JSON
    def delete(self,nota):
        global ORDER, GLOBAL_TOTAL, ITEM_VAL, GLOBAL_LABELS, GLOBAL_TOTAL_LABEL, E
        Menu_Frame.DISM, GLOBAL_TOTAL = 0, 0
        Menu_Frame.LLEVAR.set(0)
        Menu_Frame.MenuSection.checkboxLlevar.config(state='normal')
        nota.delete("1.0", "end")
        for i in E:
            i.config(state='normal')
            i.delete(0, "end")
        for i in range(len(GLOBAL_TOTAL_LABEL)):
            GLOBAL_TOTAL_LABEL[i].destroy()
        for i in range(len(ORDER)):
            ORDER.pop()
        for i in range(len(ITEM_VAL)):
            ITEM_VAL.pop()
        for i in range(len(GLOBAL_ITEM_LABELS)):
            GLOBAL_ITEM_LABELS[i].destroy()

#Display the selected items
class DisplayItems():
    def printItem(self, x, val, right):
        global GLOBAL_ITEM_LABELS, GLOBAL
        num = str(val)
        item = {x: val}
        ORDER.append(item)
        ITEM_VAL.append(val)
        if len(x) < 4:
            label = Label(TotalSection.scrollable_frame, text=x+"                        $"+num, width=40, height=1, font=("courier", 10, "bold"), anchor=W)
        elif len(x) < 8 and len(x) > 4:
            label = Label(TotalSection.scrollable_frame, text=x + "                 $" + num, width=40, height=1, font=("courier", 10, "bold"), anchor=W)
        else:
            label = Label(TotalSection.scrollable_frame, text=x + "         $" + num, width=40, height=1, font=("courier", 10, "bold"), anchor=W)

        GLOBAL_ITEM_LABELS.append(label)
        label.pack()
        if x != "Dulces" and x!= "Varios" and x!= "Barbacoa":
            self.calculate()

    #calculate the sum of the items
    def calculate(self):
        global ORDER, GLOBAL_TOTAL
        total = 0
        for i in ITEM_VAL:
            total = total + i
        GLOBAL_TOTAL = total

    #Check if it is a number. Then convert it
    def convertStr(self, d):
        if len(d)>0:
            dd= int(d)
        else :
            dd= 0
        return dd

    #store the extras and checkbox in the same JSON as the items
    def showTotal(self, right, checkbox, entrys):
        global ORDER, GLOBAL_TOTAL, GLOBAL_TOTAL_LABEL,PRESSED_TOTAL
        global E
        E = entrys
        d = entrys[0].get()
        v = entrys[1].get()
        b = entrys[2].get()
        intd, intv, intb = self.convertStr(d), self.convertStr(v), self.convertStr(b)
        self.fillEntrys(intd, intv, intb, right)
        self.set_llevar(checkbox)
        GLOBAL_TOTAL = GLOBAL_TOTAL+intd+intv+intb
        label = Label(right, text="Total= $"+str(GLOBAL_TOTAL), font=("arial", 15, "bold"), height = 4)
        GLOBAL_TOTAL_LABEL.append(label)
        label.pack()

    def set_llevar(self, checkbox):
        global ORDER
        if checkbox.get()==1:
            dicC = {"Llevar":checkbox.get()}
            ORDER.append(dicC)

    #Check for the values of the Extras
    def fillEntrys(self, d, v, b, right):
        if d!=0:
            self.printItem("Dulces", d, right)
        if v != 0:
            self.printItem("Varios", v, right)
        if b != 0:
            self.printItem("Barbacoa", b, right)


#global variables
GLOBAL_TOTAL=0
ITEM_VAL = []
ORDER = []
GLOBAL_ITEM_LABELS = []
GLOBAL_TOTAL_LABEL = []
E = None
