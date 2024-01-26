from tkinter import ttk
import matplotlib.pyplot as plt
from tkinter import *

root = Tk()
root.title("Учеба/Заполнение")
root.geometry("640x400")
root.configure(bg='#84FF00')
root.iconbitmap(default="cara.ico")



# root.resizable(False, False)


def quality(col):
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())
        num4 = int(entry4.get())
        num5 = int(entry5.get())
        num6 = int(entry6.get())
    except ValueError:
        root.title("Введите числа")
        root.iconbitmap(default="Krest.ico")
        root.configure(bg='#C70000')
    else:
        dig = 1
        it = len([(tree.set(k, col), k) for k in tree.get_children("")])
        two = num1-(num2+num3+num4)
        summ = (num2+num3) / num1 * 100
        sr = (5*num2 + 4*num3 + 3*num4 + 2*two) / num1
        kach = (num2+num3+num4) / num1 * 100
        pr = 100-(num6/(num5*num1)*100)
        qut_u = f'({num3}+{num2})/{num1}*100={summ:.0f}'
        sr_b = f'(5*{num2}+4*{num3}+3*{num4}+2*{two})/{num1}={sr:.1f}'
        kach_u = f'({num4}+{num3}+{num2})/{num1}*100={kach:.0f}'
        pr_usp = f'100-({num6}/({num1}*{num5})*100)={pr:.1f}'
        rum = [(dig+it, qut_u, sr_b, kach_u,pr_usp)]
        fil = f"{dig + it} {qut_u} {sr_b} {kach_u} {pr_usp}"
        for person in rum:
            tree.insert("", END, values=person)
        text = open('test.txt', 'r')
        a = []
        for line in text:
            a.append(line)
        text.close()
        w = ''
        for i in a:
            i1 = i.split("\n")
            w = w + i1[0] + "\n"
        text = open('test.txt', 'w')
        # str_n = f' \n' * int(len(a))
        text.write(str(w) + str(fil))
        text.close()

        root.title("Учеба/Заполнение")
        root.iconbitmap(default="cara.ico")
        root.configure(bg='#84FF00')
def sort(col, reverse):
    def takSecond(elem):
        return int(elem[1])
    # получаем все значения столбцов в виде отдельного списка
    l = [(tree.set(k, col), k) for k in tree.get_children("")]
    are = [(i[0],float((i[0].split("="))[1])) for i in l]
    are.sort(key=takSecond, reverse=reverse)
    # сортируем список
    are1 = []

    for i in are:
        for i2 in l:
            if i[0] == i2[0]:
                are1.append(i2)
    # переупорядочиваем значения в отсортированном порядке
    for index,  (_, k) in enumerate(are1):
        tree.move(k, "", index)

    # в следующий раз выполняем сортировку в обратном порядке
    tree.heading(col, command=lambda: sort(col, not reverse))

def sort1(col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children("")]

    l.sort(reverse=reverse)

    for index,  (_, k) in enumerate(l):
        tree.move(k, "", index)

    tree.heading(col, command=lambda: sort1(col, not reverse))

def diag(col):
    # получаем все значения столбцов в виде отдельного списка
    l = [(tree.set(k, col)) for k in tree.get_children("")]
    recc = [(i.split("=")) for i in l ]
    are = []
    for e in range(0,len(l)):
        are.append(recc[e][1])
    gramma = {i:are.count(i)for i in list(set(are))}
    plt.style.use('dark_background')

    x = []
    labels = []
    colors = ("green", "grey")
    for e in gramma.values():
        x.append(e)
    for e in gramma.keys():
        labels.append(e)
    fig, ax = plt.subplots(figsize=(4, 3),dpi=80)
    plt.axis('off')
    plt.ylabel('Простые числа')
    ax.pie(x, colors=colors, radius=1, labels=labels, autopct='%1.1f%%' ,startangle=90,
           wedgeprops={"linewidth": 3, "edgecolor": "white"}, frame=True)

    # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
    #        ylim=(0, 8), yticks=np.arange(1, 8))
    plt.show()


def cleaner():
    tree.delete(*tree.get_children())
    text = open('test.txt', 'w')
    text.write('')
    text.close()

lbl1 = Label(root, text="Кол-во человек", width=21, background='#84FF00')
lbl1.place(x=0, y=0, width=100, height=25)

lbl2 = Label(root, text="Число 'Оценка 5'", width=21, background='#84FF00')
lbl2.place(x=100, y=0, width=100, height=25)

lbl3 = Label(root, text="Число 'Оценка 4'", width=21, background='#84FF00')
lbl3.place(x=200, y=0, width=100, height=25)

lbl4 = Label(root, text="Число 'Оценка 3'", width=21, background='#84FF00')
lbl4.place(x=300, y=0, width=100, height=25)

lbl5 = Label(root, text="Кол-во часов", width=21, background='#84FF00')
lbl5.place(x=400, y=0, width=100, height=25)

lbl6 = Label(root, text="Кол-во пропусков", width=21, background='#84FF00')
lbl6.place(x=500, y=0, width=120, height=25)

entry1 = ttk.Entry()
entry1.place(x=0, y=30, width=125, height=25)

entry2 = ttk.Entry()
entry2.place(x=100, y=30, width=100, height=25)

entry3 = ttk.Entry()
entry3.place(x=200, y=30, width=100, height=25)

entry4 = ttk.Entry()
entry4.place(x=300, y=30, width=100, height=25)

entry5 = ttk.Entry()
entry5.place(x=400, y=30, width=100, height=25)

entry6 = ttk.Entry()
entry6.place(x=500, y=30, width=120, height=25)

btn = ttk.Button(text="Результат", width=21, command=lambda: quality(0))
btn.place(x=500, y=60, width=100, height=25)

btn = ttk.Button(text="Отчистить", width=21, command=cleaner)
btn.place(x=400, y=60, width=100, height=25)

label = ttk.Label(text="Качество успеваемости", width=29, background='#84FF00')
label.place()
# определяем столбцы
columns = ("№","cach_usp", "sr", "abs_usp","pr_usp")

tree = ttk.Treeview(columns=columns, show="headings")
tree.place(x=0, y=100, width=640, height=300)

# определяем заголовки с выпавниваем по левому краю
# tree.heading("№", text="№", anchor=W,command=lambda: sort(0, False))
# tree.heading("cach_usp", text="Качество успеваемости", anchor=W,command=lambda: sort(1, False))
# tree.heading("sr", text="Средний бал", anchor=W,command=lambda: sort(2, False))
# tree.heading("abs_usp", text="Абсолютная успеваемость", anchor=W,command=lambda: sort(3, False))
# tree.heading("pr_usp", text="% успеваемости", anchor=W,command=lambda: sort(4, False))

tree.heading("№", text="№", anchor=W,command=lambda: sort1(0,False))
tree.heading("cach_usp", text="Качество успеваемости", anchor=W,command=lambda: sort(1,False))
tree.heading("sr", text="Средний бал", anchor=W,command=lambda: sort(2,False))
tree.heading("abs_usp", text="Абсолютная успеваемость", anchor=W,command=lambda: sort(3,False))
tree.heading("pr_usp", text="% успеваемости", anchor=W,command=lambda: sort(4,False))

# настраиваем столбцы
tree.column("#1", stretch=NO, width=20)
tree.column("#2", stretch=NO, width=140)
tree.column("#3", stretch=NO, width=160)
tree.column("#4", stretch=NO, width=155)
tree.column("#5", stretch=NO, width=165)

btn = ttk.Button( width=21, command=lambda: diag(1))
btn.place(x=20, y=85, width=140, height=15)
btn = ttk.Button( width=21, command=lambda: diag(2))
btn.place(x=160, y=85, width=160, height=15)
btn = ttk.Button( width=21, command=lambda: diag(3))
btn.place(x=320, y=85, width=155, height=15)
btn = ttk.Button( width=21, command=lambda: diag(4))
btn.place(x=475, y=85, width=165, height=15)

scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x=640, y=100, width=20, height=300)

text = open('test.txt', 'r')
a = []
for line in text:
    a.append(line)
text.close()
for person in a:
    tree.insert("", END, values=person)

root.mainloop()
