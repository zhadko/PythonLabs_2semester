from tkinter import *
from tkinter import messagebox as mb
from random import randrange

class Main:
    def __init__(self):
        menubar=Menu(root)
        menubar.add_command(label="Вікно 2", command=self.win2)
        menubar.add_command(label="Вікно 3", command=self.win3)
        menubar.add_command(label="Вікно 4", command=self.win4)
        menubar.add_command(label="Вікно 5", command=self.win5)
        root.config(menu=menubar)

        first = Label(root, text="П.І.Б", bd=15, bg="khaki", fg="black", font=("Arial 18 bold"))
        first.grid(column=0,ipadx=65, sticky="w")
        second = Label(root, text="Номер групи", bd=15, bg="#ffdb4d", fg="black", font=("Arial 18 bold"))
        second.grid(column=0,ipadx=15, sticky="w")
        third = Label(root, text="Номер у списку", bd=15, bg="khaki", fg="black", font=("Arial 18 bold"))
        third.grid(column=0,sticky="w")
        forth = Label(root, text="Номер варіанту", bd=15, bg="#ffdb4d", fg="black", font=("Arial 18 bold"))
        forth.grid(column=0,sticky="w")

        self.firstEntry=Entry(root,width=20, bd=2, font="Arial 18 bold")
        self.secondEntry=Entry(root,width=20, bd=2, font="Arial 18 bold")
        self.thirdEntry=Entry(root,width=20, bd=2, font="Arial 18 bold")
        self.fourthText=Text(root,width=20,height=1, bd=2, font="Arial 18 bold")
        but1 = Button(root, width=15, height=2, text="Отримати варіант", font=("Arial 10"), command=self.variant, bg="#ffdb4d")
        self.firstEntry.grid(row=0,column=1)
        self.secondEntry.grid(row=1,column=1)
        self.thirdEntry.grid(row=2,column=1)
        self.fourthText.grid(row=3,column=1)
        but1.grid(row=4,column=1)

        capacity = Label(root, text="Потужність", bd=15, bg="#00cc99", fg="black", font=("Arial 18 bold"))
        capacity.grid(column=3, row=0)
        elements = Label(root, text="Елементи(x1 x2 x3...)", bd=15, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        elements.grid(column=4, row=0)
        A= Label(root, text="A", bd=15, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        A.grid(column=2, row=1)
        B = Label(root, text="B", bd=15, bg="#00cc99", fg="black", font=("Arial 18 bold"))
        B.grid(column=2, row=2)
        C = Label(root, text="C", bd=15, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        C.grid(column=2, row=3)

        self.capAEntry = Entry(root, width=8, bd=2, font="Arial 14 bold")
        self.capBEntry = Entry(root, width=8, bd=2, font="Arial 14 bold")
        self.capCEntry = Entry(root, width=8, bd=2, font="Arial 14 bold")
        self.capAEntry.grid(row=1, column=3)
        self.capBEntry.grid(row=2, column=3)
        self.capCEntry.grid(row=3, column=3)

        self.elAEntry = Entry(root, width=20, bd=2, font="Arial 14 bold")
        self.elBEntry = Entry(root, width=20, bd=2, font="Arial 14 bold")
        self.elCEntry = Entry(root, width=20, bd=2, font="Arial 14 bold")
        self.elAEntry.grid(row=1, column=4)
        self.elBEntry.grid(row=2, column=4)
        self.elCEntry.grid(row=3, column=4)
        but2 = Button(root, width=15, height=2, text="Random", font=("Arial 10"), command=self.random, bg="#00cc99")
        but2.grid(row=4, column=4)

        universal = Label(root, text="Універсальна множина - U", bd=15, bg="#ff6666", fg="black", font=("Arial 18 bold"))
        universal.grid(row=5, column=0, columnspan=2, sticky="w", pady=20)
        start = Label(root, text="Від", bd=5, fg="black",font=("Arial 15"))
        end = Label(root, text="До", bd=5, fg="black",font=("Arial 15"))
        start.grid(row=6, column=0, sticky="w")
        end.grid(row=6, column=0, padx=60, sticky="e")
        self.startEntry = Entry(root, width=5, bd=2, font="Arial 14 bold")
        self.endEntry = Entry(root, width=5, bd=2, font="Arial 14 bold")
        self.startEntry.grid(row=6, column=0, padx=40, sticky="w")
        self.endEntry.grid(row=6, column=0, sticky="e")

        but3 = Button(root, width=18, height=2, text="Зберегти дані", font=("Arial 12"), command=self.save, bg="#0099ff")
        but3.grid(row=7, column=4)

        root.config(menu=menubar)

    def win2(self):
        self.wid2=Toplevel(root)
        self.wid2.title("Вікно 2")
        self.wid2.geometry("800x400")
        A = Label(self.wid2, text="A", bd=10, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        A.grid(column=0, row=0)
        B = Label(self.wid2, text="B", bd=10, bg="#00cc99", fg="black", font=("Arial 18 bold"))
        B.grid(column=0, row=1)
        C = Label(self.wid2, text="C", bd=10, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        C.grid(column=0, row=2)
        D = Label(self.wid2, text="D", bd=10, bg="#00cc99", fg="black", font=("Arial 18 bold"))
        D.grid(column=0, row=3)
        but4 = Button(self.wid2, width=18, height=2, text="Зберегти дані", font=("Arial 12"), command=self.save_D, bg="#0099ff")
        but4.grid(row=4, column=0, columnspan=2, rowspan=2)

        self.elA = Entry(self.wid2, width=20, bd=2, font="Arial 14 bold")
        self.elB = Entry(self.wid2, width=20, bd=2, font="Arial 14 bold")
        self.elC = Entry(self.wid2, width=20, bd=2, font="Arial 14 bold")
        self.elD = Entry(self.wid2, width=20, bd=2, font="Arial 14 bold")
        self.elA.grid(row=0, column=1)
        self.elB.grid(row=1, column=1)
        self.elC.grid(row=2, column=1)
        self.elD.grid(row=3, column=1)
        self.saveD = ((self.saveA | self.saveB) | self.saveC | (self.saveB | self.saveC) | self.saveA)
        self.elA.delete(0, END)
        self.elA.insert(INSERT, list(self.saveA))
        self.elB.delete(0, END)
        self.elB.insert(INSERT, list(self.saveB))
        self.elC.delete(0, END)
        self.elC.insert(INSERT, list(self.saveC))

        step1 = Button(self.wid2, width=20, height=2, text="Крок 1", font=("Arial 12"), command=self.step1long, bg="#cc66ff")
        step1.grid(row=0, column=2)
        step2 = Button(self.wid2, width=20, height=2, text="Крок 2", font=("Arial 12"), command=self.step2long, bg="#cc66ff")
        step2.grid(row=1, column=2)
        step3 = Button(self.wid2, width=20, height=2, text="Крок 3", font=("Arial 12"), command=self.step3long, bg="#cc66ff")
        step3.grid(row=2, column=2)
        step4 = Button(self.wid2, width=20, height=2, text="Крок 4", font=("Arial 12"), command=self.step4long,bg="#cc66ff")
        step4.grid(row=3, column=2)
        step5 = Button(self.wid2, width=20, height=2, text="Крок 5", font=("Arial 12"), command=self.step5long,bg="#cc66ff")
        step5.grid(row=4, column=2)

    def win3(self):
        self.wid3=Toplevel(root)
        self.wid3.title("Вікно 3")
        self.wid3.geometry("800x400")
        A = Label(self.wid3, text="A", bd=10, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        A.grid(column=0, row=0)
        B = Label(self.wid3, text="B", bd=10, bg="#00cc99", fg="black", font=("Arial 18 bold"))
        B.grid(column=0, row=1)
        C = Label(self.wid3, text="C", bd=10, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        C.grid(column=0, row=2)
        D = Label(self.wid3, text="D", bd=10, bg="#00cc99", fg="black", font=("Arial 18 bold"))
        D.grid(column=0, row=3)
        but4 = Button(self.wid3, width=18, height=2, text="Зберегти дані", font=("Arial 12"), command=self.save_Dshort,bg="#0099ff")
        but4.grid(row=4, column=0, columnspan=2, rowspan=2)

        self.elA = Entry(self.wid3, width=20, bd=2, font="Arial 14 bold")
        self.elB = Entry(self.wid3, width=20, bd=2, font="Arial 14 bold")
        self.elC = Entry(self.wid3, width=20, bd=2, font="Arial 14 bold")
        self.elD = Entry(self.wid3, width=20, bd=2, font="Arial 14 bold")
        self.elA.grid(row=0, column=1)
        self.elB.grid(row=1, column=1)
        self.elC.grid(row=2, column=1)
        self.elD.grid(row=3, column=1)
        self.saveD = ((self.saveB | self.saveC) | self.saveA)
        self.elA.delete(0, END)
        self.elA.insert(INSERT, list(self.saveA))
        self.elB.delete(0, END)
        self.elB.insert(INSERT, list(self.saveB))
        self.elC.delete(0, END)
        self.elC.insert(INSERT, list(self.saveC))

        step1 = Button(self.wid3, width=20, height=2, text="Крок 1", font=("Arial 12"), command=self.step2short,bg="#cc66ff")
        step1.grid(row=0, column=2)
        step2 = Button(self.wid3, width=20, height=2, text="Крок 2", font=("Arial 12"), command=self.step4short,bg="#cc66ff")
        step2.grid(row=1, column=2)

    def win4(self):
        self.wid4 = Toplevel(root)
        self.wid4.title("Вікно 4")
        self.wid4.geometry("800x400")
        X = Label(self.wid4, text="X", bd=10, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        X.grid(column=0, row=0)
        Y = Label(self.wid4, text="Y", bd=10, bg="#00cc99", fg="black", font=("Arial 18 bold"))
        Y.grid(column=0, row=1)
        Z = Label(self.wid4, text="Z", bd=10, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        Z.grid(column=0, row=2)

        self.elX = Entry(self.wid4, width=20, bd=2, font="Arial 14 bold")
        self.elY = Entry(self.wid4, width=20, bd=2, font="Arial 14 bold")
        self.elZ = Entry(self.wid4, width=20, bd=2, font="Arial 14 bold")
        self.elX.grid(row=0, column=1)
        self.elY.grid(row=1, column=1)
        self.elZ.grid(row=2, column=1)
        self.elX.delete(0, END)
        self.elX.insert(INSERT, list(self.saveB))
        self.elY.delete(0, END)
        self.elY.insert(INSERT, list(self.notC))

        but5 = Button(self.wid4, width=16, height=2, text="Обчислити Z", font=("Arial 10"), command=self.calcZ, bg="#cc66ff")
        but5.grid(column=2, row=2)
        but6 = Button(self.wid4, width=18, height=2, text="Зберегти дані", font=("Arial 12"), command=self.save_Z,bg="#0099ff")
        but6.grid(row=4, column=0, columnspan=2, pady=100)

    def win5(self):
        self.wid5 = Toplevel(root)
        self.wid5.title("Вікно 5")
        self.wid5.geometry("800x400")
        X = Label(self.wid5, text="X", bd=10, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        X.grid(column=0, row=0)
        Y = Label(self.wid5, text="Y", bd=10, bg="#00cc99", fg="black", font=("Arial 18 bold"))
        Y.grid(column=0, row=1)
        Z = Label(self.wid5, text="Z", bd=10, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        Z.grid(column=0, row=2)
        Dlong = Label(self.wid5, text="Dlong", bd=10, bg="#00cc99", fg="black", font=("Arial 18 bold"))
        Dlong.grid(column=0, row=3,columnspan=2, sticky="w")
        Dshort = Label(self.wid5, text="Dshort", bd=10, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        Dshort.grid(column=0, row=4,columnspan=2, sticky="w")
        Z1 = Label(self.wid5, text="Z1", bd=10, bg="#00cc99", fg="black", font=("Arial 18 bold"))
        Z1.grid(column=0, row=5,columnspan=2, sticky="w")
        Z2 = Label(self.wid5, text="Z2", bd=10, bg="#99ff99", fg="black", font=("Arial 18 bold"))
        Z2.grid(column=0, row=6,columnspan=2, sticky="w")

        self.el2X = Entry(self.wid5, width=20, bd=2, font="Arial 14 bold")
        self.el2Y = Entry(self.wid5, width=20, bd=2, font="Arial 14 bold")
        self.el2Z = Entry(self.wid5, width=20, bd=2, font="Arial 14 bold")
        self.el2X.grid(row=0, column=1)
        self.el2Y.grid(row=1, column=1)
        self.el2Z.grid(row=2, column=1)
        self.el2X.delete(0, END)
        self.el2X.insert(INSERT, list(self.saveB))

        step1 = Button(self.wid5, width=20, height=2, text="Крок 1", font=("Arial 12"), command=self.step1forZ,bg="#cc66ff")
        step1.grid(row=0, column=2)
        step2 = Button(self.wid5, width=20, height=2, text="Крок 2", font=("Arial 12"), command=self.step2forZ,bg="#cc66ff")
        step2.grid(row=1, column=2)
        but6 = Button(self.wid5, width=18, height=2, text="Зберегти Z2", font=("Arial 12"), command=self.save_Z2,bg="#0099ff")
        but6.grid(row=6, column=2)
        but7 = Button(self.wid5, width=18, height=2, text="Зчитати дані", font=("Arial 12"), command=self.getdata,bg="#0099ff")
        but7.grid(row=5, column=3, columnspan=1)
        but6 = Button(self.wid5, width=18, height=2, text="Порівняти D", font=("Arial 12"), command=self.compD,bg="#00cc99")
        but6.grid(row=2, column=2, columnspan=1)
        but7 = Button(self.wid5, width=18, height=2, text="Порівняти Z", font=("Arial 12"), command=self.compZ,bg="#00cc99")
        but7.grid(row=3, column=2, columnspan=1)

        self.DlongEntry = Entry(self.wid5, width=18, font=("Arial 13"))
        self.DlongEntry.grid(row=3, column=1, sticky="e")
        self.DshortEntry = Entry(self.wid5, width=18, font=("Arial 13"))
        self.DshortEntry.grid(row=4, column=1, sticky="e")
        self.Z1Entry = Entry(self.wid5, width=18, font=("Arial 13"))
        self.Z1Entry.grid(row=5, column=1, sticky="e")
        self.Z2Entry = Entry(self.wid5, width=18, font=("Arial 13"))
        self.Z2Entry.grid(row=6, column=1, sticky="e")

    def getdata(self):
        with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab1\saveDlong.txt', "r", encoding="utf-8") as r:
            self.DlongEntry.delete(0, END)
            self.DlongEntry.insert(INSERT, r.readline())
        with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab1\saveDshort.txt', "r", encoding="utf-8") as r:
            self.DshortEntry.delete(0, END)
            self.DshortEntry.insert(INSERT, r.readline())
        with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab1\saveZ1.txt', "r", encoding="utf-8") as r:
            self.Z1Entry.delete(0, END)
            self.Z1Entry.insert(INSERT, r.readline())
        with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab1\saveZ2.txt', "r", encoding="utf-8") as r:
            self.Z2Entry.delete(0, END)
            self.Z2Entry.insert(INSERT, r.readline())

    def calcZ(self):
        self.saveZ=set()
        for el in self.saveB:
            self.saveZ.add(el)
        for el in self.notC:
            if el not in self.saveB:
                self.saveZ.add(el)
            elif el in self.saveB:
                self.saveZ.remove(el)
        self.elZ.delete(0, END)
        self.elZ.insert(INSERT, self.saveZ)

    def compD(self):
        if list(self.DlongEntry.get()) == list(self.DshortEntry.get()):
            mess1 = Label(self.wid5, text="Dlong=Dshort={}".format(self.DshortEntry.get()), bd=5, fg="black",font=("Arial 12"))
            mess1.grid(column=3, row=2, sticky="w")
    def compZ(self):
        if list(self.Z1Entry.get()) == list(self.Z2Entry.get()):
            mess2 = Label(self.wid5, text="Z1=Z2={}".format(self.Z2Entry.get()), bd=5, fg="black",font=("Arial 12"))
            mess2.grid(column=3, row=3, sticky="w")
        else:
            mess2 = Label(self.wid5, text="Z1!=Z2={}".format(self.Z2Entry.get()), bd=5, fg="black", font=("Arial 12"))
            mess2.grid(column=3, row=3, sticky="w")

    def step1long(self):
        step1lable=Label(self.wid2, text="A∪B={}".format(self.saveA|self.saveB), bd=5, fg="black", font=("Arial 15"))
        step1lable.grid(column=3, row=0, sticky="w")
    def step2long(self):
        step2lable=Label(self.wid2, text="B∪C={}".format(self.saveB|self.saveC), bd=5, fg="black", font=("Arial 15"))
        step2lable.grid(column=3, row=1, sticky="w")
    def step2short(self):
        step3lable=Label(self.wid3, text="B∪C={}".format(self.saveB|self.saveC), bd=5, fg="black", font=("Arial 15"))
        step3lable.grid(column=3, row=0, sticky="w")
    def step3long(self):
        step3lable=Label(self.wid2, text="(A∪B)∪C={}".format((self.saveA|self.saveB)|self.saveC), bd=5, fg="black", font=("Arial 15"))
        step3lable.grid(column=3, row=2, sticky="w")
    def step4long(self):
        step4lable=Label(self.wid2, text="(B∪C)∪A={}".format((self.saveB|self.saveC)|self.saveA), bd=5, fg="black", font=("Arial 15"))
        step4lable.grid(column=3, row=3, sticky="w")
    def step4short(self):
        self.elD.delete(0, END)
        self.elD.insert(INSERT, self.saveD)
        step4short=Label(self.wid3, text="D=(B∪C)∪A={}".format((self.saveB|self.saveC)|self.saveA), bd=5, fg="black", font=("Arial 15"))
        step4short.grid(column=3, row=1, sticky="w")
    def step5long(self):
        self.elD.delete(0, END)
        self.elD.insert(INSERT, self.saveD)
        step5lable=Label(self.wid2, text="D=((A∪B)∪C)∪((B∪C)∪A)={}".format(self.saveD), bd=5, fg="black", font=("Arial 13"))
        step5lable.grid(column=3, row=4, sticky="w")
    def step1forZ(self):
        self.el2Y.delete(0, END)
        self.el2Y.insert(INSERT, list(self.saveU - self.saveC))
        step1short = Label(self.wid5, text="-C=U-C={}".format(self.saveU - self.saveC), bd=5,fg="black", font=("Arial 15"))
        step1short.grid(column=3, row=0, sticky="w")
    def step2forZ(self):
        self.saveZ2 = (self.saveB ^ (self.saveU - self.saveC))
        self.el2Z.delete(0, END)
        self.el2Z.insert(INSERT, self.saveZ2)
        step2short = Label(self.wid5, text="Z=B^(-C)={}".format(self.saveZ2), bd=5, fg="black",font=("Arial 15"))
        step2short.grid(column=3, row=1, sticky="w")

    def random(self):
        A,B,C=set(),set(),set()
        try:
            capA=int(self.capAEntry.get())
            capB=int(self.capBEntry.get())
            capC=int(self.capCEntry.get())
            while len(A) !=capA:
                A.add(randrange(256))
            self.elAEntry.delete(0, END)
            self.elAEntry.insert(INSERT, list(A))
            while len(B) !=capB:
                B.add(randrange(256))
            self.elBEntry.delete(0, END)
            self.elBEntry.insert(INSERT, list(B))
            while len(C) !=capC:
                C.add(randrange(256))
            self.elCEntry.delete(0, END)
            self.elCEntry.insert(INSERT, list(C))
        except ValueError:
            msg="Введіть числові дані"
            mb.showerror("Error", msg)

    def variant(self):
        try:
            N = int(self.secondEntry.get())
            G = int(self.thirdEntry.get())
            self.fourthText.delete(1.0, END)
            self.fourthText.insert(INSERT, (N+G%60)%30+1)
        except ValueError:
            msg = "Введіть числові дані"
            mb.showerror("Error", msg)

    def save(self):
        self.saveA=set()
        for el in str(self.elAEntry.get()).split():
            self.saveA.add(int(el))
        self.saveB=set()
        for el in str(self.elBEntry.get()).split():
            self.saveB.add(int(el))
        self.saveC=set()
        for el in str(self.elCEntry.get()).split():
            self.saveC.add(int(el))
        try:
            self.saveU=set()
            for el in range(int(self.startEntry.get()), int(self.endEntry.get())+1):
                self.saveU.add(el)
        except ValueError:
            msg = "Введіть діапазон універсальної множини"
            mb.showerror("Error", msg)
        self.notC = self.saveU
        for el in self.saveC:
            if el in self.notC:
                self.notC.remove(el)

    def save_D(self):
        with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab1\saveDlong.txt', "a", encoding="utf-8") as w:
            w.write(str(self.saveD)+"\n")
    def save_Dshort(self):
        with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab1\saveDshort.txt', "a", encoding="utf-8") as w:
            w.write(str(self.saveD)+"\n")
    def save_Z(self):
        with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab1\saveZ1.txt', "a", encoding="utf-8") as w:
            w.write(str(self.saveZ)+"\n")
    def save_Z2(self):
        with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab1\saveZ2.txt', "a", encoding="utf-8") as w:
            w.write(str(self.saveZ2)+"\n")

root = Tk()
root.geometry("1000x600")
root.title('Lab1')
obj=Main()
root.mainloop()