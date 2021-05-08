from tkinter import *
from options_pricing import Options

root = Tk()
root.title('Options Graph')
root.geometry('600x600')

ticker = Entry(root, width=20)
ticker.grid(row=1, column=1, padx=30)
strike = Entry(root, width=20)
strike.grid(row=2, column=1, padx=30)

ticker.insert(0, 'AAPL')


def myClick():
    stock = Options(ticker.get())
    stock.calls(strike.get(), 1679011200)

myButton = Button(root, text='Graph', command=myClick)
myButton.grid()


root.mainloop()