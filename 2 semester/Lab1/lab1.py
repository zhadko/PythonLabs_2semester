def variant(self):
    try:
        N = int(self.secondEntry.get())
        G = int(self.thirdEntry.get())
        self.fourthText.delete(1.0, END)
        self.fourthText.insert(INSERT, (N + G % 60) % 30 + 1)
    except ValueError:
        self.fourthText.delete(1.0, END)
        self.fourthText.insert(INSERT, "Введіть числові дані")

def union(x, y):
    z = x
    for el in y:
        if el not in x:
            z.add(el)
    return z

def sim_dif(x, y):
    s = x
    for el in y:
        if el not in x:
            s.add(el)
        elif el in x:
            s.remove(el)
    return s

def notFunc(X, U):
    notX = U
    for el in X:
        if el in notX:
            notX.remove(el)
    return notX

def func1(A, B, C):
    if union(union(union(A, B), C), union(union(B, C), A))==(B | C) | A==union((union(B, C)), A):
        print("Спрощення виконано правильно")
    print(union(union(union(A, B), C), union(union(B, C), A)))
    print(union((union(B, C)), A))
    print((A | B) | C | (B | C) | A)
    print((B | C) | A)

def func2(B, C, U):
    print(sim_dif(B, (notFunc(C, U))))

func1({1, 2}, {3}, {4})
func2({3}, {4}, {1, 2, 3, 4})