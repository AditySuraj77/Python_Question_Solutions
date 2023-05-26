from currency_converter import CurrencyConverter
from tkinter import *

root = Tk()

root.title('Currancy converter')
root.geometry('500x500')
conv = CurrencyConverter()


def clicked():
    amount = int(amount_entry.get())
    currancy = currancy_entry.get()
    conv_currancy = currancy_name_conv_entry.get()
    data = conv.convert(amount, currancy, conv_currancy)
    result_label = Label(root, text=f'{conv_currancy} {round(data, 2)}',font=('Verdana 20'))
    result_label.place(x=230, y=290)


heading = Label(root, text='Currancy Converter', font=('Verdana 25 bold'))
heading.pack(padx=5, pady=5)

amount = Label(root, text='Amount', font=('Verdana 20')).place(x=20, y=100)

currancy_name = Label(root, text='Currany Name', font=('Verdana 20')).place(x=20, y=150)

currancy_name_conv = Label(root, text='Convert Currency', font=('Verdana 20')).place(x=20, y=200)

amount_entry = Entry(root)
amount_entry.place(x=300, y=110)

currancy_entry = Entry(root)
currancy_entry.place(x=300, y=160)

currancy_name_conv_entry = Entry(root)
currancy_name_conv_entry.place(x=300, y=211)

result_btn = Button(root, text='Submit', command=clicked)
result_btn.place(x=200, y=250)

root.mainloop()

# curr_conv = conv.convert(100,'USD','INR')
# print(curr_conv)
