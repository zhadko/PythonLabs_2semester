from tkinter import *
from tkinter import messagebox as mb
import random

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
        but1 = Button(root, width=15, height=2, text="Отримати варіант", font=("Arial 10"), command=self.variant, bg="#ffdb4d")
        firstEntry.grid(row=0, column=1)
        self.secondEntry.grid(row=1, column=1)
        self.thirdText.grid(row=2, column=1)
        but1.grid(row=3, column=1)

        root.config(menu=menubar)

    def win2(self):
        self.wid2 = Toplevel(root)
        self.wid2.title("Вікно 2")
        self.wid2.geometry("1400x700")

        head1 = Label(self.wid2, text="Задайте множину імен через пробіл", bd=10, fg="black", font=("Arial 18 bold"))
        head1.grid(column=0, row=0, columnspan=5)
        self.namesEntry = Entry(self.wid2, width=105, bd=2, font="Arial 10 bold")
        self.namesEntry.grid(column=0, row=1, columnspan=5)

        self.names=["Ганна", "Дарина", "Софія", "Юлія", "Надія", "Олена", "Людмила", "Євгенія",
                    "Артем", "Назар", "Влад", "Стас", "Кирило", "Матвій", "Андрій", "Роман"]

        but1 = Button(self.wid2, width=20, height=2, text="Задати випадково", font=("Arial 10"), command=self.randomListOfNames, bg="#ffdb4d")
        but1.grid(row=1, column=5, columnspan=1)

        head2 = Label(self.wid2, text="Задайте множину віку через пробіл", bd=10, fg="black", font=("Arial 18 bold"))
        head2.grid(column=0, row=3, columnspan=5)
        self.agesEntry = Entry(self.wid2, width=40, bd=2, font="Arial 14 bold")
        self.agesEntry.grid(column=0, row=4, columnspan=5, rowspan=2)

        self.ages = [16, 18, 19, 22, 21, 24, 29, 30, 31, 45, 38, 50, 49, 55, 63, 70]

        but2 = Button(self.wid2, width=20, height=2, text="Задати випадково", font=("Arial 10"), command=self.randomListOfAges, bg="#ffdb4d")
        but2.grid(row=5, column=5, columnspan=1)

        but3 = Button(self.wid2, width=30, height=2, text="Сформувати базову множину", font=("Arial 10"), command=self.saveToDict, bg="#ffdb4d")
        but3.grid(row=8, column=0, columnspan=5)

        head3 = Label(self.wid2, text="Задайте кількість показників віку за якими здійснити відбір", bd=10, fg="black", font=("Arial 18 bold"))
        head3.grid(column=0, row=12, columnspan=5)
        self.KEntry = Entry(self.wid2, width=10, bd=2, font="Arial 18 bold")
        self.KEntry.grid(column=5, row=12, columnspan=1)

        head4 = Label(self.wid2, text="Введіть показники", bd=10, fg="black", font=("Arial 18 bold"))
        head4.grid(column=0, row=13, columnspan=1)
        self.indicatorsEntry = Entry(self.wid2, width=50, bd=2, font="Arial 14 bold")
        self.indicatorsEntry.grid(column=1, row=13, columnspan=4)
        but4 = Button(self.wid2, width=20, height=2, text="Задати випадково", font=("Arial 10"), command=self.randomListToGet, bg="#ffdb4d")
        but4.grid(row=13, column=5, columnspan=1)

        but6 = Button(self.wid2, width=20, height=2, text="Вибірка з базової множини", font=("Arial 10"), command=self.algorithmOfSearch, bg="#ffdb4d")
        but6.grid(row=14, column=0, columnspan=5)
    def variant(self):
        try:
            NZK = int(self.secondEntry.get())
            self.thirdText.delete(1.0, END)
            self.thirdText.insert(INSERT, (NZK % 26) + 1)
        except ValueError:
            msg = "Введіть числові дані"
            mb.showerror("Error", msg)

    def randomListOfNames(self):
        random.shuffle(self.names)
        self.namesEntry.delete(0, END)
        self.namesEntry.insert(INSERT, self.names)

    def randomListOfAges(self):
        random.shuffle(self.ages)
        self.agesEntry.delete(0, END)
        self.agesEntry.insert(INSERT, self.ages)

    def randomListToGet(self):
        arr = random.sample(self.ages, int(self.KEntry.get()))
        self.indicatorsEntry.delete(0, END)
        self.indicatorsEntry.insert(INSERT, arr)

    def saveToDict(self):
        self.mainDict=dict()
        for i in range(0, len(self.namesEntry.get().split())):
            self.mainDict[self.namesEntry.get().split()[i]]=self.agesEntry.get().split()[i]
        head3 = Label(self.wid2, text="Базова множина: {}".format(self.mainDict), bd=10, fg="black", font=("Arial 10"))
        head3.grid(column=0, row=9, columnspan=9, rowspan=2)

        arr1 = list(self.mainDict.values())
        arr2 = list(self.mainDict.keys())
        self.QuickSort(0, len(arr1)-1, arr1, arr2)

        self.sortedDict=dict()
        for i in range(0, len(arr1)):
            self.sortedDict[arr2[i]]=arr1[i]
        head5 = Label(self.wid2, text="Резутьтат сортування: {}".format(self.sortedDict), bd=10, fg="black", font=("Arial 10"))
        head5.grid(column=0, row=11, columnspan=9)

    def QuickSort(self, l, r, arr1, arr2):
        def partition(l, r, nums, names):
            # Last element will be the pivot and the first element the pointer
            pivot, ptr = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    # Swapping values smaller than the pivot to the front
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    names[i], names[ptr] = names[ptr], names[i]
                    ptr += 1
            # Finally swapping the last element with the pointer indexed number
            nums[ptr], nums[r] = nums[r], nums[ptr]
            names[ptr], names[r] = names[r], names[ptr]
            return ptr

        if l < r:
            pi = partition(l, r, arr1, arr2)
            self.QuickSort(l, pi - 1, arr1, arr2)  # Recursively sorting the left values
            self.QuickSort(pi + 1, r, arr1, arr2)  # Recursively sorting the right values

    def algorithmOfSearch(self):
        choosenAge = self.indicatorsEntry.get().split()
        x = (1 + len(self.sortedDict.values())) // 2
        self.finalDict=dict()
        for el in choosenAge:
            if el<list(self.sortedDict.values())[x]:
                for i in range(0,x):
                    if el==list(self.sortedDict.values())[i]:
                        key=list(self.sortedDict.keys())[i]
                        self.finalDict[key]=self.sortedDict.get(key)
            else:
                for i in range(x,len(self.sortedDict.values())):
                    if el==list(self.sortedDict.values())[i]:
                        key=list(self.sortedDict.keys())[i]
                        self.finalDict[key]=self.sortedDict.get(key)
        head7 = Label(self.wid2, text="Резутьтат вибірки: {}".format(self.finalDict), bd=10, fg="black", font=("Arial 14"))
        head7.grid(column=0, row=15, columnspan=9)

        arr1 = list(self.finalDict.values())
        arr2 = list(self.finalDict.keys())
        self.QuickSort(0, len(arr1) - 1, arr1, arr2)

        self.sortedFinalDict = dict()
        for i in range(0, len(arr1)):
            self.sortedFinalDict[arr2[i]] = arr1[i]
        head7 = Label(self.wid2, text="Відсортований результат вибірки: {}".format(self.sortedFinalDict), bd=10, fg="black",font=("Arial 14"))
        head7.grid(column=0, row=16, columnspan=9)


root = Tk()
root.geometry("700x400")
root.title('Lab5')
obj = Main()
root.mainloop()