import pyautogui
import pyperclip
import tagui
import pyautogui as py
import time
from tkinter import *
def busca():
    py.PAUSE = 0.5

janela = Tk()
janela.geometry('400x400')
entry1 = Entry(janela)
entry1.place(x=20, y=50, height=20, width=200)
entry2 = Entry(janela)
entry2.place(x=20, y=100, height=20, width=200)
entry3 = Entry(janela)
entry3.place(x=20, y=150, height=20, width=200)
entry4 = Entry(janela,)
entry4.place(x=20, y=200, height=20, width=200)
label1 = Label(janela, text='')
label1.place(x=20, y=20)
label2 = Label(janela, text='')
label2.place(x=20, y= 70)
label3 = Label(janela, text='')
label3.place(x=20, y=120)
label4 = Label(janela, text='')
label4.place(x=20, y=170)
btn1 = Button(janela, command=busca).place(x=20, y=300, width=50, height=20)
janela.mainloop()
