from tkinter import *
window = Tk()
window.title("Entry WIzard")
Label(window, text='First Name',bg="Red").grid(row=0)
Label(window, text='Last Name').grid(row=1)
first = Entry(window)
second = Entry(window)
first.grid(row=0,column=1)
second.grid(row=1, column=1)
mainloop()
