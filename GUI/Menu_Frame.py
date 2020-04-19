
from tkinter import *
from Total_Frame import DisplayItems

class MenuSection(object):
    def __init__(self, left, right):
        container = Frame(left, borderwidth=2, relief="solid")
        checkbox = self.Checkboxes(left)
        left.pack(side="left", expand=True, fill="both")
        container.pack(expand=True, fill="both", padx=10, pady=10)
        Menu(container, right, checkbox)

    def Checkboxes(self, left):
        global LLEVAR
        LLEVAR = IntVar()
        #aqui = IntVar()
        checkboxContainer = Frame(left)
        checkboxContainer.pack()

        checkboxLlevar = Checkbutton(checkboxContainer, text="Llevar", variable=LLEVAR)
        #checkboxAqui = Checkbutton(checkboxContainer, text="Aqui", variable=aqui)
        checkboxLlevar.pack(side=LEFT, fill="both", padx=10, pady=10)
        #checkboxAqui.pack(fill="both", padx=10, pady=10)
        return LLEVAR

class Menu(object):
    def __init__(self, container, right, checkbox):
        container_left = Frame(container, borderwidth=2)
        container_middle = Frame(container, borderwidth=2)
        container_right = Frame(container, borderwidth=2)
        container_left.pack(side= "left", expand=True, fill="both", padx=10, pady=10)
        container_middle.pack(side= "left", expand=True, fill="both", padx=10, pady=10)
        container_right.pack(side= "right", expand=True, fill="both", padx=10, pady=10)

        food = {"1 kilo": 360, "3/4": 270, "1/2": 180, "1/4": 90, "Orden": 55, "Torta": 55, "Burrito": 35, "Consome Chico": 65, "Consome Grande": 105}
        beverage = {"Refresco de Vidrio":17, "Refresco de Plastico":19, "Cafe Regular":17, "Cafe Capuccino":27, "Bebida Infantil":17, "Botella de Agua":10}
        extras = {"1 Paq de Tortillas":20, "1/2 Paq de Tortillas":10, "PZ de Pan Blanco":8, "Pz de Tortilla de Harina":8}
        text = ["Dulces", "Varios", "Barbacoa"]
        self.fillMenu(food, container_left, right)
        self.fillMenu(beverage, container_middle, right)
        self.fillMenu(extras, container_right, right)
        entrys = self.setEntry(container_middle, text)
        done_button = Button(container_right, text="ver total", command= lambda: self.disableButton(right, checkbox, entrys), height= 4, width= 30, font=("arial", 10, "bold"), bg="orange")
        done_button.pack(side=BOTTOM)

    def disableButton(self, right, checkbox, entrys):
        global DISB
        global DISM
        if DISB ==0:
            DisplayItems().showTotal(right, checkbox, entrys)
        DISB = 1
        DISM = 1

    def setEntry(self, container, t):
        entrys=[]
        for i in t:
            L1 = Label(container, text=i, font=("arial", 10, "bold"))
            L1.pack()
            E1 = Entry(container, bd=3)
            E1.pack()
            entrys.append(E1)
        return entrys

    def fillMenu(self, item, container, right):
        for i in item:
            button = Button(container, text=i, command= lambda key=i, val=item[i]: self.disableMenu(key, val, right), height= 4, width= 30)
            button.pack(fill = BOTH)

    def disableMenu(self, key, val, right):
        global DISM
        if DISM == 0:
            DisplayItems().printItem(key, val, right)

DISB= 0
DISM = 0
LLEVAR = 0