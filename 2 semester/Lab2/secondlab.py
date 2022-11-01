from tkinter import *
from tkinter import messagebox as mb


class Main:
    def __init__(self):
        menubar = Menu(root)
        menubar.add_command(label="Вікно 2", command=self.win2)
        menubar.add_command(label="Вікно 3", command=self.win3)
        menubar.add_command(label="Вікно 4", command=self.win4)
        root.config(menu=menubar)

        first = Label(root, text="П.І.Б", bd=15, bg="khaki", fg="black", font=("Arial 18 bold"))
        first.grid(column=0, ipadx=65, sticky="w")
        second = Label(root, text="Номер групи", bd=15, bg="#ffdb4d", fg="black", font=("Arial 18 bold"))
        second.grid(column=0, ipadx=15, sticky="w")
        third = Label(root, text="Номер у списку", bd=15, bg="khaki", fg="black", font=("Arial 18 bold"))
        third.grid(column=0, sticky="w")
        forth = Label(root, text="Номер варіанту", bd=15, bg="#ffdb4d", fg="black", font=("Arial 18 bold"))
        forth.grid(column=0, sticky="w")

        self.firstEntry = Entry(root, width=20, bd=2, font="Arial 18 bold")
        self.secondEntry = Entry(root, width=20, bd=2, font="Arial 18 bold")
        self.thirdEntry = Entry(root, width=20, bd=2, font="Arial 18 bold")
        self.fourthText = Text(root, width=20, height=1, bd=2, font="Arial 18 bold")
        but1 = Button(root, width=15, height=2, text="Отримати варіант", font=("Arial 10"), command=self.variant,bg="#ffdb4d")
        self.firstEntry.grid(row=0, column=1)
        self.secondEntry.grid(row=1, column=1)
        self.thirdEntry.grid(row=2, column=1)
        self.fourthText.grid(row=3, column=1)
        but1.grid(row=4, column=1)

        root.config(menu=menubar)

    def win2(self):
        global A, B
        self.A = set()
        self.B = set()
        self.wid2 = Toplevel(root)
        self.wid2.title("Вікно 2")
        self.wid2.geometry("400x400")

        self.var = IntVar()
        head1 = Label(self.wid2, text="Виберіть елементи для множини:", fg="black", font=("Arial 10"))
        head1.grid(column=0, row=0, columnspan=2)
        self.a_checkbutton = Radiobutton(self.wid2, text="A", value=1, variable=self.var, padx=15, pady=10)
        self.a_checkbutton.grid(row=0, column=2, sticky=W)
        self.b_checkbutton = Radiobutton(self.wid2, text="B", value=2, variable=self.var, padx=15, pady=10)
        self.b_checkbutton.grid(row=0, column=3, sticky=W)

        self.names1 = ["Ганна", "Дарина", "Софія", "Діана", "Марія", "Вікторія", "Тетяна", "Юлія", "Надія", "Олена",
                       "Людмила", "Євгенія"]
        self.names1_listbox = Listbox(self.wid2, width=20, height=8, selectmode=MULTIPLE, exportselection=False)
        for name in self.names1:
            self.names1_listbox.insert(END, name)
        self.names1_listbox.grid(row=1, column=0, columnspan=2)

        self.names2 = ["Артем", "Назар", "Влад", "Стас", "Кирило", "Матвій", "Андрій", "Роман", "Пилип", "Віталій",
                       "Яромир", "Прохор"]
        self.names2_listbox = Listbox(self.wid2, width=20, height=8, selectmode=MULTIPLE, exportselection=False)
        for name in self.names2:
            self.names2_listbox.insert(END, name)
        self.names2_listbox.grid(row=1, column=2, columnspan=2)

        self.head2 = LabelFrame(self.wid2, text="Дії над вибраною множиною", font='Arial 10')
        self.head2.grid(row=2, column=1, columnspan=2)

        copybut = Button(self.head2, width=16, height=1, text="Зберегти дані", font=("Arial 12"), command=self.save_el,
                         bg="#0099ff")
        copybut.grid(row=0, )
        getbut = Button(self.head2, width=16, height=1, text="Зчитати дані", font=("Arial 12"), command=self.get_el,
                        bg="#0099ff")
        getbut.grid(row=1)
        clearbut = Button(self.head2, width=16, height=1, text="Очистити дані", font=("Arial 12"),
                          command=self.clear_el, bg="#0099ff")
        clearbut.grid(row=2, )

        self.getA = Label(self.wid2, text="A=()\n", font=("Arial 10"))
        self.getA.grid(row=3, column=0, columnspan=4)
        self.getB = Label(self.wid2, text="B=()\n", font=("Arial 10"))
        self.getB.grid(row=4, column=0, columnspan=4)

    def win3(self):
        self.wid3 = Toplevel(root)
        self.wid3.title("Вікно 3")
        self.wid3.geometry("400x700")

        self.headA = LabelFrame(self.wid3, text="Множина А", font='Arial 10')
        self.headA.grid(row=0, column=0, columnspan=2)
        self.headB = LabelFrame(self.wid3, text="Множина В", font='Arial 10')
        self.headB.grid(row=0, column=2, columnspan=2)

        self.listboxofA = Listbox(self.headA, width=20, height=7, selectmode=SINGLE, exportselection=False)
        for name in list(self.A):
            self.listboxofA.insert(END, name)
        self.listboxofA.grid(row=0, column=0, columnspan=1)
        self.listboxofB = Listbox(self.headB, width=20, height=7, selectmode=SINGLE, exportselection=False)
        for name in list(self.B):
            self.listboxofB.insert(END, name)
        self.listboxofB.grid(row=0, column=0, columnspan=1)

        addpairtoS = Button(self.wid3, width=20, height=1, text="Сформувати пару до S", font=("Arial 12"),
                            command=self.buildS, bg="#0099ff")
        addpairtoS.grid(row=1, column=1, columnspan=2)
        addpairtoR = Button(self.wid3, width=20, height=1, text="Сформувати пару до R", font=("Arial 12"),
                            command=self.buildR, bg="#0099ff")
        addpairtoR.grid(row=2, column=1, columnspan=2)

        self.showS = Label(self.wid3, text="", font="Arial 8")
        self.showS.grid(row=4, column=0, columnspan=4)
        self.showR = Label(self.wid3, text="", font="Arial 8")
        self.showR.grid(row=5, column=0, columnspan=4)
        self.errormessage = Label(self.wid3, text="", font="Arial 8", fg="red")
        self.errormessage.grid(row=3, column=0, columnspan=4)

        self.dictofS = dict()
        self.familiesofR = list()
        self.listofR = list()
        self.listofusedR = list()

        self.canvS = Canvas(self.wid3, width=400, height=200)
        self.dict_SA = {}
        self.dict_SB = {}
        self.canvS.create_text(160, 30, text='а чоловік b', font='Arial 12 bold')
        for i in range(len(self.A)):
            self.canvS.create_text(30 + i * 50, 50, text=list(self.A)[i], font='Arial 10')
            self.canvS.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
            self.dict_SA.update({list(self.A)[i]: [30 + i * 50, 80]})
        for j in range(len(self.B)):
            self.canvS.create_text(30 + j * 50, 190, text=list(self.B)[j], font='Arial 10')
            self.canvS.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="blue")
            self.dict_SB.update({list(self.B)[j]: [30 + j * 50, 160]})
        self.canvS.grid(row=6, column=0, columnspan=4)

        self.canvR = Canvas(self.wid3, width=400, height=200)
        self.dict_RA = {}
        self.dict_RB = {}
        self.canvR.create_text(160, 30, text='а брат b', font='Arial 12 bold')
        for i in range(len(self.A)):
            self.canvR.create_text(30 + i * 50, 50, text=list(self.A)[i], font='Arial 10')
            self.canvR.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
            self.dict_RA.update({list(self.A)[i]: [30 + i * 50, 80]})
        for j in range(len(self.B)):
            self.canvR.create_text(30 + j * 50, 190, text=list(self.B)[j], font='Arial 10')
            self.canvR.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="blue")
            self.dict_RB.update({list(self.B)[j]: [30 + j * 50, 160]})
        self.canvR.grid(row=7, column=0, columnspan=4)

    def win4(self):
        self.wid4 = Toplevel(root)
        self.wid4.title("Вікно 4")
        self.wid4.geometry("800x400")

        unionbut = Button(self.wid4, width=6, height=1, text="R ∪ S", font=("Arial 12"), command=self.union,
                          bg="#0099ff")
        unionbut.grid(row=1, column=0, columnspan=1)
        crossbut = Button(self.wid4, width=6, height=1, text="R ∩ S", font=("Arial 12"), command=self.crossing,
                          bg="#0099ff")
        crossbut.grid(row=2, column=0, columnspan=1)
        diffbut = Button(self.wid4, width=6, height=1, text="R \ S", font=("Arial 12"), command=self.difference,
                         bg="#0099ff")
        diffbut.grid(row=3, column=0, columnspan=1)
        addbut = Button(self.wid4, width=6, height=1, text="U \ R", font=("Arial 12"), command=self.addition,
                        bg="#0099ff")
        addbut.grid(row=4, column=0, columnspan=1)
        revaddbut = Button(self.wid4, width=6, height=1, text="S^-1", font=("Arial 12"), command=self.reversaladdition,
                           bg="#0099ff")
        revaddbut.grid(row=5, column=0, columnspan=1)

        self.headtext = Label(self.wid4, text="", font="Arial 12 bold")
        self.headtext.grid(row=0, column=1, columnspan=4)
        self.canvofactRS = Canvas(self.wid4, width=400, height=200)
        self.topdict = {}
        self.bottomdict = {}
        for i in range(len(self.A)):
            self.canvofactRS.create_text(30 + i * 50, 50, text=list(self.A)[i], font='Arial 10')
            self.canvofactRS.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
            self.topdict.update({list(self.A)[i]: [30 + i * 50, 80]})
        for j in range(len(self.B)):
            self.canvofactRS.create_text(30 + j * 50, 190, text=list(self.B)[j], font='Arial 10')
            self.canvofactRS.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="blue")
            self.bottomdict.update({list(self.B)[j]: [30 + j * 50, 160]})
        self.canvofactRS.grid(row=1, column=1, columnspan=4, rowspan=5)

    def variant(self):
        try:
            N = int(self.secondEntry.get())
            G = int(self.thirdEntry.get())
            self.fourthText.delete(1.0, END)
            self.fourthText.insert(INSERT, (N + G % 60) % 30 + 1)
        except ValueError:
            msg = "Введіть числові дані"
            mb.showerror("Error", msg)

    def save_el(self):
        match self.var.get():
            case 1:
                for i in self.names1_listbox.curselection():
                    self.A.add(self.names1_listbox.get(i))
                for i in self.names2_listbox.curselection():
                    self.A.add(self.names2_listbox.get(i))
                with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab2\saveA.txt', "a", encoding="utf-8") as w:
                    w.write(str(self.A) + "\n")
            case 2:
                for i in self.names1_listbox.curselection():
                    self.B.add(self.names1_listbox.get(i))
                for i in self.names2_listbox.curselection():
                    self.B.add(self.names2_listbox.get(i))
                with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab2\saveB.txt', "a", encoding="utf-8") as w:
                    w.write(str(self.B) + "\n")

    def get_el(self):
        match self.var.get():
            case 1:
                with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab2\saveA.txt', "r", encoding="utf-8") as r:
                    self.getA["text"] = "A={}".format(r.readline())
            case 2:
                with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab2\saveB.txt', "r", encoding="utf-8") as r:
                    self.getB["text"] = "B={}\n".format(r.readline())

    def clear_el(self):
        match self.var.get():
            case 1:
                with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab2\saveA.txt', "w") as f:
                    f.write("")
            case 2:
                with open(r'C:\Users\Admin\Desktop\универ\Programing\2 sem\Lab2\saveB.txt', "w") as f:
                    f.write("")

    def buildS(self):
        a = self.listboxofA.get(self.listboxofA.curselection())
        b = self.listboxofB.get(self.listboxofB.curselection())
        if a in self.names2 and b in self.names1 and a not in self.dictofS.keys() and b not in self.dictofS.values():
            if a in self.listofusedR and b in self.listofusedR:
                self.errormessage["text"] = "'a' can not be a brother of 'b'"
            else:
                self.dictofS[a] = b
                self.canvS.create_line(self.dict_SA[a], self.dict_SB[b], arrow=LAST)
        else:
            self.errormessage["text"] = "'a' can not be a husband of 'b'"
        self.showS["text"] = "S={}".format(self.dictofS)

    def buildR(self):
        a = self.listboxofA.get(self.listboxofA.curselection())
        b = self.listboxofB.get(self.listboxofB.curselection())
        error = 0
        if a in self.names2 and a != b and a not in self.dictofS.keys():
            if a not in self.listofusedR and b not in self.listofusedR:
                self.familiesofR.append([a, b])
                self.listofusedR.append(a)
                self.listofusedR.append(b)
                self.listofR.append([a, b])
                self.canvR.create_line(self.dict_RA[a], self.dict_RB[b], arrow=LAST)
            elif len(self.familiesofR) > 0:
                for el in self.familiesofR:
                    if a in el and b in el:
                        break
                    elif a in el or b in el:
                        for k, v in self.dictofS.items():
                            if v == b and k in el:
                                error = 1
                                break
                            elif k == b and v in el:
                                error = 1
                                break
                        if error == 0 and a in el and b not in self.listofusedR:
                            el.append(b)
                            self.listofusedR.append(b)
                            self.listofR.append([a, b])
                            self.canvR.create_line(self.dict_RA[a], self.dict_RB[b], arrow=LAST, tag="lines")
                        elif error == 0 and b in el and a not in self.listofusedR:
                            el.append(a)
                            self.listofusedR.append(a)
                            self.listofR.append([a, b])
                            self.canvR.create_line(self.dict_RA[a], self.dict_RB[b], arrow=LAST, tag="lines")
                    if error == 1:
                        self.errormessage["text"] = "'a' can not be a brother of 'b'"
                        break
        elif a in self.names2 and a != b and self.dictofS[a] != b:
            if a not in self.listofusedR and b not in self.listofusedR:
                self.familiesofR.append([a, b])
                self.listofusedR.append(a)
                self.listofusedR.append(b)
                self.listofR.append([a, b])
                self.canvR.create_line(self.dict_RA[a], self.dict_RB[b], arrow=LAST)
            elif len(self.familiesofR) > 0:
                for el in self.familiesofR:
                    if self.dictofS[a] in el:
                        continue
                    elif a in el and b in el:
                        break
                    elif a in el or b in el:
                        for k, v in self.dictofS.items():
                            if v == b and k in el:
                                error = 1
                                break
                            elif k == b and v in el:
                                error = 1
                                break
                        if error == 0 and a in el and b not in self.listofusedR:
                            el.append(b)
                            self.listofusedR.append(b)
                            self.listofR.append([a, b])
                            self.canvR.create_line(self.dict_RA[a], self.dict_RB[b], arrow=LAST)
                        elif error == 0 and b in el and a not in self.listofusedR:
                            el.append(a)
                            self.listofusedR.append(a)
                            self.listofR.append([a, b])
                            self.canvR.create_line(self.dict_RA[a], self.dict_RB[b], arrow=LAST)
                    if error == 1:
                        self.errormessage["text"] = "'a' can not be a brother of 'b'"
                        break
        else:
            self.errormessage["text"] = "'a' can not be a brother of 'b'"
        self.showR["text"] = "R={}".format(self.familiesofR)

    def union(self):
        for k, v in self.dictofS.items():
            self.canvofactRS.create_line(self.topdict[k], self.bottomdict[v], arrow=LAST, tag="lines")
        for k, v in self.listofR:
            self.canvofactRS.create_line(self.topdict[k], self.bottomdict[v], arrow=LAST, fill='red', tag="lines")
        self.headtext["text"] = 'R ∪ S'

    def crossing(self):
        self.canvofactRS.delete("lines")
        self.headtext["text"] = 'Перетину немає'

    def difference(self):
        self.canvofactRS.delete("lines")
        for k, v in self.dictofS.items():
            self.canvofactRS.create_line(self.topdict[k], self.bottomdict[v], arrow=LAST, tag="lines")
        for k, v in self.listofR:
            self.canvofactRS.create_line(self.topdict[k], self.bottomdict[v], arrow=LAST, fill='red', tag="lines")
        self.headtext["text"] = 'R \ S'

    def addition(self):
        self.canvofactRS.delete("lines")
        for k in self.A:
            for v in self.B:
                if [k, v] in self.listofR:
                    continue
                else:
                    self.canvofactRS.create_line(self.topdict[k], self.bottomdict[v], arrow=LAST, tag="lines")
        self.headtext["text"] = 'U \ R'

    def reversaladdition(self):
        self.canvofactRS.delete("all")
        self.canvofactRS.delete("lines")
        for i in range(len(self.B)):
            self.canvofactRS.create_text(30 + i * 50, 50, text=list(self.B)[i], font='Arial 10')
            self.canvofactRS.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="blue")
            self.topdict.update({list(self.B)[i]: [30 + i * 50, 80]})
        for j in range(len(self.A)):
            self.canvofactRS.create_text(30 + j * 50, 190, text=list(self.A)[j], font='Arial 10')
            self.canvofactRS.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="green")
            self.bottomdict.update({list(self.A)[j]: [30 + j * 50, 160]})
        self.canvofactRS.grid(row=1, column=1, columnspan=4, rowspan=5)
        for k, v in self.dictofS.items():
            self.canvofactRS.create_line(self.topdict[v], self.bottomdict[k], arrow=LAST, tag="lines")
        self.headtext["text"] = 'S^-1'


root = Tk()
root.geometry("1000x600")
root.title('Lab1')
obj = Main()
root.mainloop()
