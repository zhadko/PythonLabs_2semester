from tkinter import *
from tkinter import messagebox as mb
import random
import networkx as nx
import pylab as plt

class Main:
    def __init__(self):
        menubar = Menu(root)
        menubar.add_command(label="Вікно 2", command=self.win2)
        root.config(menu=menubar)

        first = Label(root, text="П.І.Б", bd=15, bg="khaki", fg="black", font=("Arial 18 bold"))
        first.grid(column=0, ipadx=67, sticky="w")
        second = Label(root, text="Номер з.к.", bd=15, bg="#ffdb4d", fg="black", font=("Arial 18 bold"))
        second.grid(column=0, ipadx=32, sticky="w")
        third = Label(root, text="Номер варіанту", bd=15, bg="khaki", fg="black", font=("Arial 18 bold"))
        third.grid(column=0, sticky="w")

        firstEntry = Entry(root, width=20, bd=2, font="Arial 18 bold")
        self.secondEntry = Entry(root, width=20, bd=2, font="Arial 18 bold")
        self.thirdText = Text(root, width=20, height=1, bd=2, font="Arial 18 bold")
        but1 = Button(root, width=15, height=2, text="Отримати варіант", font=("Arial 10"), command=self.variant,
                      bg="#ffdb4d")
        firstEntry.grid(row=0, column=1)
        self.secondEntry.grid(row=1, column=1)
        self.thirdText.grid(row=2, column=1)
        but1.grid(row=3, column=1)

        root.config(menu=menubar)

    def win2(self):
        self.wid2 = Toplevel(root)
        self.wid2.title("Вікно 2")
        self.wid2.geometry("700x500")

        V = Label(self.wid2, text="Кількість вершин", bd=15, bg="khaki", fg="black", font=("Arial 18 bold"))
        V.grid(column=0, row=0, columnspan=5)
        self.VEntry = Entry(self.wid2, width=20, bd=2, font="Arial 18 bold")
        self.VEntry.grid(column=5, row=0, columnspan=5)

        but1 = Button(self.wid2, width=20, height=2, text="Сформувати матрицю", font=("Arial 10"),
                      command=self.doMatrix, bg="#ffdb4d")
        but1.grid(row=0, column=10)

        self.head1 = LabelFrame(self.wid2, text="Матриця суміжності", font='Arial 10')
        self.head1.grid(row=3, column=0, columnspan=10)

    def variant(self):
        try:
            NZK = int(self.secondEntry.get())
            self.thirdText.delete(1.0, END)
            self.thirdText.insert(INSERT, (NZK % 10) + 1)
        except ValueError:
            msg = "Введіть числові дані"
            mb.showerror("Error", msg)

    def random_gen(self):
        self.tabl = [[0] * self.v for i in range(self.v)]
        for i in range(self.v):
            for j in range(self.v):
                if i == j:
                    pass
                else:
                    self.tabl[i][j] = random.randint(0, 1)
                    self.tabl[j][i] = self.tabl[i][j]
        for i in range(self.v):
            for j in range(0,i):
                self.Cij[i][j].delete(0, END)
                self.Cij[i][j].insert(INSERT, self.tabl[i][j])

    def doMatrix(self):
        self.v = int(self.VEntry.get())

        for i in range(0, self.v + 1):
            for j in range(0, self.v + 1):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    Label(self.head1, text='{}'.format(j), font='Arial 16 bold', width=3).grid(column=j, row=i,
                                                                                               sticky=W)
                elif j == 0:
                    Label(self.head1, text='{}'.format(i), font='Arial 16 bold', width=3).grid(column=j, row=i, sticky=W)

        self.Cij = []
        for i in range(0,self.v):
            self.Cij.append([])
            for j in range(0,i+1):
                self.Cij[i].append(Entry(self.head1, font='Arial 14', width=3))
                self.Cij[i][j].grid(row=i + 1, column=j + 1, sticky=W)
                if i == j:
                    self.Cij[i][j].insert(INSERT, '0')

        random = Button(self.wid2, text='Згенерувати випадково', font='Arial 12', bg='#ffdb4d', command=self.random_gen)
        random.grid(column=0, columnspan=10, row=4)

        but2 = Button(self.wid2, width=30, height=2, text="Показати розфарбований граф", font=("Arial 10"),
                      command=self.show_coloredGraph, bg="#ffdb4d")
        but2.grid(row=5, column=0, columnspan=10)

    def show_coloredGraph(self):
        colors = ["Red", "Blue", "Green", "Pink", "Yellow"]
        colorV = ["None"] * self.v
        v = self.v
        Arr = [[0] * v for i in range(v)]
        for i in range(v):
            for j in range(0,i+1):
                if i == j:
                    pass
                else:
                    Arr[i][j] = int(self.Cij[i][j].get())
                    Arr[j][i] = Arr[i][j]

        def visit(i):
            for c in colors:
                CN = True
                for j in range(0, v):
                    if (Arr[j][i] == 1) and (colorV[j] == c):
                        CN = False
                        break
                if CN:
                    colorV[i] = c
                    break
            if i+1!=v:
                visit(i + 1)
        visit(0)

        my_graph = nx.Graph()
        listOfGetter = [[] for l in range(v)]
        for i in range(0, v):
            for j in range(0, i):
                if Arr[i][j] != 0:
                    my_graph.add_edge(i + 1, j + 1)
                    listOfGetter[j].append(i)

        nodePosition = nx.circular_layout(my_graph)
        nx.draw_networkx(my_graph, nodePosition)
        for i in range(len(colorV)):
            nx.draw_networkx(my_graph, nodePosition, nodelist=[(i + 1)], node_color=colorV[i])
        plt.show()

root = Tk()
root.geometry("700x400")
root.title('Lab4')
obj = Main()
root.mainloop()
