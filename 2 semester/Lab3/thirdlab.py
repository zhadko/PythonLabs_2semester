from tkinter import *
from tkinter import messagebox as mb
import math
import networkx as nx
import pylab as plt

class Main:
    def __init__(self):
        menubar = Menu(root)
        menubar.add_command(label="Вікно 2", command=self.win2)
        menubar.add_command(label="Вікно 3", command=self.win3)
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
        self.wid2.geometry("700x400")

        V = Label(self.wid2, text="Кількість вершин", bd=15, bg="khaki", fg="black", font=("Arial 18 bold"))
        V.grid(column=0, row=0, columnspan=5)
        self.VEntry = Entry(self.wid2, width=20, bd=2, font="Arial 18 bold")
        self.VEntry.grid(column=5, row=0, columnspan=5)

        but1 = Button(self.wid2, width=20, height=2, text="Сформувати матрицю", font=("Arial 10"),
                      command=self.doMatrix, bg="#ffdb4d")
        but1.grid(row=0, column=10)
        self.but2 = Button(self.wid2, width=20, height=2, text="Записати рядок матриці", font=("Arial 10"),
                           command=self.saveRowToMatrix, bg="#ffdb4d")
        self.but2.grid(row=2, column=10)

        self.head1 = LabelFrame(self.wid2, text="Матриця ваг", font='Arial 10')
        self.head1.grid(row=3, column=0, columnspan=10)
        self.headMessage = Label(self.wid2, text="Введіть елементи 1-ого рядка через пробіл(inf=∞)", bd=15, fg="black", font=("Arial 14 bold"))
        self.headMessage.grid(column=0, row=1, columnspan=10)
        self.CRow = Entry(self.wid2, width=50, bd=2, font="Arial 12")
        self.CRow.grid(column=0, row=2, columnspan=10)

        self.i = 0

    def win3(self):
        self.wid3 = Toplevel(root)
        self.wid3.title("Вікно 3")
        self.wid3.geometry("700x400")

        self.TableOfIndex=[[0] * self.v for i in range(self.v)]
        for j in range(1, self.v):
            self.TableOfIndex[j][0] = math.inf
        for k in range(1, self.v):
            for m in range(1,self.v):
                a=set()
                for l in range(0, self.v):
                    a.add(self.TableOfIndex[l][k-1] + self.Cij[l][m])
                self.TableOfIndex[m][k]=min(a)

        but1 = Button(self.wid3, width=20, height=2, text="Показати таблицю індексів", font=("Arial 10"),command=self.show_Table, bg="#ffdb4d")
        but1.grid(row=0, column=0)

        headMessage2 = Label(self.wid3, text="Введіть номер вершини для визначення її найкоротшого шляху", bd=15, fg="black",font=("Arial 12 bold"))
        headMessage2.grid(column=0, row=2, columnspan=4)
        self.node = Entry(self.wid3, width=10, bd=2, font="Arial 12")
        self.node.grid(column=4, row=2)

        self.result = Label(self.wid3, text="", bd=15,fg="black", font=("Arial 14 bold"))
        self.result.grid(column=2, row=3, columnspan=2)

        but2 = Button(self.wid3, width=20, height=2, text="Показати граф", font=("Arial 10"),command=self.show_Graph, bg="#ffdb4d")
        but2.grid(row=3, column=0, columnspan=2)

    def variant(self):
        try:
            NZK = int(self.secondEntry.get())
            self.thirdText.delete(1.0, END)
            self.thirdText.insert(INSERT, (NZK % 6) + 1)
        except ValueError:
            msg = "Введіть числові дані"
            mb.showerror("Error", msg)

    def doMatrix(self):
        self.v = int(self.VEntry.get())
        self.Cij = [[0] * self.v for i in range(self.v)]

    def saveRowToMatrix(self):
        self.Cij[self.i] = self.CRow.get().split(" ")
        self.CRow.delete(0, END)
        self.i += 1
        self.headMessage["text"] = "Введіть елементи {}-ого рядка через пробіл".format(self.i + 1)
        if self.i == self.v:
            self.headMessage["text"] = "Матриця ваг успішно сформована"
            for i in range(0, self.v):
                for j in range(0, self.v):
                    cell = Entry(self.head1, width=5, bd=2, font="Arial 12")
                    cell.grid(row=i, column=j)
                    cell.insert(INSERT, self.Cij[i][j])
                    try:
                        self.Cij[i][j]=int(self.Cij[i][j])
                    except:
                        self.Cij[i][j] = math.inf

    def show_Table(self):
        head2 = LabelFrame(self.wid3, text="Таблиця індексів", font='Arial 10')
        head2.grid(row=1, column=0)
        for i in range(0, self.v):
            for j in range(0, self.v):
                cell = Entry(head2, width=5, bd=2, font="Arial 12")
                cell.grid(row=i, column=j)
                cell.insert(INSERT, self.TableOfIndex[i][j])

    def show_Graph(self):
        node=int(self.node.get())
        my_graph = nx.DiGraph()
        res = [node]
        listOfGetter = [[] for i in range(self.v)]
        for i in range(0, self.v):
            for j in range(0, self.v):
                if self.Cij[i][j] != math.inf:
                    my_graph.add_edge(i + 1, j + 1, color="black", weight=self.Cij[i][j])
                    listOfGetter[j].append(i)
        for n in range(self.v, 1, -1):
            for i in listOfGetter[node - 1]:
                if self.TableOfIndex[i][n - 2] + self.Cij[i][node - 1] == self.TableOfIndex[node - 1][n - 1]:
                    node = i + 1
                    res.append(node)
                    break
        res = list(reversed(res))
        self.result["text"]="{}".format(res)
        for i in range(1, len(res)):
            pre = res[i - 1]
            post = res[i]
            my_graph.add_edge(pre, post, color='red', weight=self.Cij[pre - 1][post - 1])
        edges = my_graph.edges()

        colors = [my_graph[u][v]['color'] for u, v in edges]
        weights = [my_graph[u][v]['weight'] for u, v in edges]

        nodePosition = nx.circular_layout(my_graph)
        nx.draw(my_graph, nodePosition, with_labels=True, font_weight='bold', edge_color=colors, width=weights)
        plt.show()

root = Tk()
root.geometry("700x400")
root.title('Lab3')
obj = Main()
root.mainloop()
