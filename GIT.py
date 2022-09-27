import pyautogui
import pyperclip
import tagui
import pyautogui as py
import time
from tkinter import *
def busca():
    py.PAUSE = 1
    py.leftClick(20, 745)
    py.write(f'Pasta: {str(entry1.get())}')
    py.press('Enter')
    py.leftClick(1125, 160)
    py.write(str(entry2.get()))
    py.press('Enter')
    py.rightClick(195, 220)
    py.leftClick(266, 556)
    time.sleep(1)
    py.leftClick(20, 745)
    py.write('Pasta: REPOSITORIO_LOCAL_GIT')
    py.press('Enter')
    py.leftClick(1125, 160)
    py.write(str(entry3.get()))
    py.press('enter')
    py.doubleClick(195, 220)
    py.rightClick(0, 230)
    py.leftClick(6, 368)
    py.leftClick(630, 220)
    py.rightClick(1150, 220)
    py.leftClick(1023, 447)


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
label1 = Label(janela, text='Nome da pasta onde está o projeto (PyCharmProjects).')
label1.place(x=20, y=20)
label2 = Label(janela, text='Nome do arquivo a ser commitado (dentro da pasta)')
label2.place(x=20, y= 70)
label3 = Label(janela, text='Pasta onde será colado o projeto par fazer o commit')
label3.place(x=20, y=120)
label4 = Label(janela, text='')
label4.place(x=20, y=170)
btn1 = Button(janela, command=busca).place(x=20, y=300, width=50, height=20)
janela.mainloop()
