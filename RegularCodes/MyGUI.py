#homework: display on label what person have selected from radio button
#store customer input of message from customer askquestion
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Menu

window = Tk()#to create window,this should be first line

m = Menu(window)
new_item = Menu(m)#giving it memory in space
new_item.add_command(label="new")
new_item.add_command(label="open")
new_item.add_separator()
new_item.add_command(label="exit")
m.add_cascade(label='File', menu = new_item)
window.config(menu = m)

lblname = Label(window, text="hello")
lblname.grid(column=0, row=0)

txtname = Entry(window, width=20)
txtname.grid(column=1, row=0)

def greet():
    messagebox.showinfo("Attention", "please save your data")
    #messagebox.askquestion("Attention", "please save your data")
    #messagebox.askyesnocancel("Attention", "please save your data")
    #messagebox.askretrycancel("Attention", "please save your data")
    res="welcome"+txtname.get()
    lblname.configure(text=res)#to change text on runtime

btnsave = Button(window, text="Save", command=greet)#command given to run funtion when button is clicked
btnsave.grid(column=2, row=0)

city = Combobox(window)
city['value']=("Amritsar","dehradun","Delhi")
city.current(0)#by default wha 0th index wala ana chahie
city.grid(column=1, row=1)

rbcc = Radiobutton(window, text="credit card", value = 1)# we have to give unique value so that they can only select 1 radio button
rbdc = Radiobutton(window, text="debit card", value = 2)
rbcod = Radiobutton(window, text="COD", value = 3)
rbcc.grid(column=0, row= 2)
rbdc.grid(column=1, row= 2)
rbcod.grid(column=2, row= 2)

state = BooleanVar()
chk = Checkbutton(window, text='Sms', var=state)
chk.grid(column=0, row= 3)

window.geometry('550x400')

window.mainloop()#we have to write this to keep the window, this should be last line
