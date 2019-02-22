import tkinter as tk
#from functools import partial
from tkinter import Menu

def call_result(label_result, n1, n2, n3):
    num1 = (n1.get())
    num2 = (n2.get())
    num3 = (n3.get())
    result = float(num1)*float(num2)*float(num3)/100
    label_result.config(text="To pay... %d" % result)
    return

root = tk.Tk()
root.geometry('400x300')
root.title('Gasoline calculation')

number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()

labelTitle = tk.Label(root, text=()).grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Prais for liters").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Gas mileage").grid(row=2, column=0)
labelNum3 = tk.Label(root, text="Mileage").grid(row=3, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)
call_result = partial(call_result, labelResult, number1, number2, number3)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=7, column=2)

#Create a Menu menu_bar
root_bar = Menu(win)
root.config(menu=menu_bar)

# Create menu and add menu items
file_menu = Menu(menu_bar)
file_menu.add_command(Label="New")     #add File menu items
menu_bar.add_cascade(label="Fale", menu =file_menu)

name_entered.focus()

root.mainloop()
