from tkinter import *

class Freedom:
    def __init__(self, window):
        window.geometry('600x400')
        window.title('Freedom Units')
        window.resizable(0, 0)
        self.Fahrenheit = Entry(window, width=15, font=('calibre', 10, 'normal'))
        self.Fahrenheit.insert(0, 0)
        self.Celsius = Entry(window, width=15, font=('calibre', 10, 'normal'))
        button = Button(window, text='Calculate', width=10, font=('Times', 20), command=self.cal)
        label1 = Label(window, text='Fahrenheit', width=10, font=('Times', 15))
        label2 = Label(window, text=' is equivalent to ', width=11, font=('Times', 15))
        label3 = Label(window, text=' Celsius ', width=10, font=('Times', 15))
        button.place(x=230, y=300)
        self.Fahrenheit.place(x=275, y=105)
        self.Celsius.place(x=275, y=205)
        label1.place(x=350, y=100)
        label2.place(x=120, y=200)
        label3.place(x=350, y=200)

    def cal(self):
        self.Celsius.delete(0, END)
        Far_val = float(self.Fahrenheit.get())
        self.Celsius.insert(END, round(((Far_val - 32) * 5.0 / 9.0),2))

root = Tk()
app = Freedom(root)
root.mainloop()
