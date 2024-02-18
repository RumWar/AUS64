from tkinter import *
import matplotlib.pyplot as plt
from tkinter import ttk, Listbox


def dig():
    e = languages_listbox.size()
    if e == 1:
        labels = []
        m = languages_listbox.get(0)
        labels.append(m)
    else:
        labels = list(map(str, languages_listbox.get(0, e)))

    e1 = languages_listbox1.size()
    if e1 == 1:
        values = []
        m = languages_listbox1.get(0)
        values.append(float(m))
    else:
        values = list(map(float, languages_listbox1.get(0, e1)))
    if len(labels) == len(values):
        fig1, ax1 = plt.subplots()
        num1 = language_entry2.get()
        ax1.pie(values, labels=labels, autopct='%1f%%')
        fig1.suptitle(f'{num1}')
        root.configure(bg='#fff')
        plt.show()
    else:
        root.configure(bg='#f00')



# функции удаление выделенного элемента
def delete():
    selection = languages_listbox.curselection()
    languages_listbox.delete(selection[0])


def delete1():
    selection = languages_listbox1.curselection()
    languages_listbox1.delete(selection[0])


# добавление новых элемента
def add1():
    new_language = language_entry1.get()
    languages_listbox1.insert(0, new_language)


def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)


root = Tk()
root.title("Диаграмма на соц опрос")
root.iconbitmap(r'D:\pythonden4\test\пр соц опрос\icon.ico')
root.geometry("550x340")
root.resizable(False, False)
# root.columnconfigure(index=0, weight=6)
# root.columnconfigure(index=1, weight=1)
# root.rowconfigure(index=0, weight=1)
# root.rowconfigure(index=1, weight=3)
# root.rowconfigure(index=2, weight=1)

# текстовое поле и кнопка для добавления в список
language = ttk.Label(text="Название")
language.grid(column=0, row=0, padx=6, pady=6)
language_entry = ttk.Entry()

language = ttk.Label(text="Числа")
language.grid(column=3, row=0, padx=6, pady=6)
language_entry = ttk.Entry()

language_entry.grid(column=0, row=1, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=1, padx=6, pady=6)

language_entry1 = ttk.Entry()
language_entry1.grid(column=3, row=1, padx=6, pady=6, sticky=W)
ttk.Button(text="Добавить", command=add1).grid(column=4, row=1, padx=6, pady=6)
# создаем список
languages_listbox = Listbox()
languages_listbox.grid(row=2, column=0, columnspan=2, sticky=EW, padx=5, pady=5)

languages_listbox1 = Listbox()
languages_listbox1.grid(row=2, column=3, columnspan=2, sticky=EW, padx=5, pady=1)

ttk.Button(text="Удалить", command=delete).grid(row=3, column=1, padx=5, pady=5)

ttk.Button(text="Удалить", command=delete1).grid(row=3, column=4, padx=5, pady=5)

language_entry2 = ttk.Entry(width=70)
language_entry2.place(x=10, y=285)

language2 = ttk.Label(text="Название диаграммы",width=20)
language2.place(x=5, y=255)
ttk.Button(text="Диаграмма", command=dig).grid(column=6, row=8, padx=6, pady=6)

root.mainloop()
