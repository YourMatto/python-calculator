from tkinter import *
from tkinter import ttk

def calculate():
    try:
        using = usings.get()
        if using == "+":
            try:
                a = float(aDigid.get())
                b = float(bDigid.get())
                answer.set(int(a + b))
            except ValueError:
                pass
        elif using == "-":
            try:
                a = float(aDigid.get())
                b = float(bDigid.get())
                answer.set(int(a - b))
            except ValueError:
                pass
        elif using == "/":
            try:
                a = float(aDigid.get())
                b = float(bDigid.get())
                answer.set(int(a / b))
            except ValueError:
                pass
        elif using == "*":
            try:
                a = float(aDigid.get())
                b = float(bDigid.get())
                answer.set(int(a * b))
            except ValueError:
                pass
        else:
            answer.set("wrong option")
    except ValueError:
        pass

root = Tk()
root.title("Calc")
root.resizable(False, False)
root.iconbitmap('calculator.ico')
#root.geometry("800x400")

mainframe = ttk.Frame(root, padding="3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

aDigid = StringVar()
aDigid = ttk.Entry(mainframe, width=10, textvariable=aDigid)
aDigid.grid(column=1, row=2, sticky=(W, E))

bDigid = StringVar()
bDigid = ttk.Entry(mainframe, width=10, textvariable=bDigid)
bDigid.grid(column=3, row=2, sticky=(W, E))

answer = StringVar()
ttk.Label(mainframe, textvariable=answer).grid(column=2, row=3, sticky=(W, E))

usings = StringVar()
using = ttk.Combobox(mainframe, textvariable=usings)
using.grid(column=2, row=2,sticky=(W, E))
using['values'] = ('+', '-', '/', '*')
using.configure(width=1)

ttk.Label(mainframe, text="Answer:").grid(column=1, row=3, sticky=W)

ttk.Button(mainframe, text="calculate", command=calculate).grid(column=3, row=3, sticky=N)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()