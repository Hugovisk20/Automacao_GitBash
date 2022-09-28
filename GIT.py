import pyautogui
import pyperclip
import tagui
import pyautogui as py
import time
from tkinter import *
def busca():
    #AUTOMATIZANDO A CÓPIA DO ARQUIVO DO PROJETO PARA OUTRA PASTA PARA FAZER O COMMIT
    py.PAUSE = 1
    py.leftClick(20, 745) #CLICA NO BOTÃO WINDOWS
    py.write(f'Pasta: {str(entry1.get())}') #ESCREVE O ENTRY1 NA BARRA DE PESQUISA DO WINDOWS PROCURANDO POR PASTAS
    py.press('Enter') #PRESSIONA A TECLA ENTER
    py.leftClick(1125, 160) #CLICA NA BARRA DE PESQUISA DA PASTA
    py.write(str(entry2.get())) #ESCREVE O ENTRY2 NA BARRA DE PESQUISA DA PASTA
    py.press('Enter') #PRESSIONA A TECLA ENTER
    py.rightClick(195, 220) #CLICA COM O DIREITO DO MOUSE NO 1º ARQUIVO
    py.leftClick(266, 556) #COPIA O ARQUIVO
    time.sleep(1) #ESPERA 1 SEGUNDO PARA EXECUTAR O PRÓXIMO CÓDIGO
    py.leftClick(20, 745) #CLICA NO BOTÇAO WINDOWS
    py.write('Pasta: REPOSITORIO_LOCAL_GIT') #PESQUISA PELA PASTA
    py.press('Enter') #PRESSIONA ENTER
    py.leftClick(1125, 160) #CLICA NA BARRA DE PESQUISA DA PASTA
    py.write(str(entry3.get())) #ESCREVE O ENTRY3 NA BARRA DE PESQUISA DA PASTA
    py.press('enter') #PRESSIONA ENTER
    py.doubleClick(195, 220) #DOUBLECLICK NO PRIMEIRO ARQUIVO
    py.rightClick(0, 230) #CLICA COM O DIREITO NO CANTO DA TELA
    py.leftClick(6, 368) #CLICA COM O ESQUERDO EM COLAR
    py.leftClick(630, 220) # CLICA EM SUBSTITUIR ARQUIVO

    #AUTOMATIZANDO GITBASH
    py.rightClick(1150, 220)
    py.leftClick(1023, 447)
    time.sleep(2)
    py.leftClick(395, 188)
    py.write('git status')
    time.sleep(0.5)
    py.write(f'git add {str(entry4.get())}')
    time.sleep(0.5)
    py.write(f'git commit -m "{str(entry4.get())}"')
    time.sleep(0.5)
    py.write('git status')
    time.sleep(0.5)
    py.write('git push')

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
label4 = Label(janela, text='Nome no qual o commit vai ser chamado')
label4.place(x=20, y=170)
btn1 = Button(janela, command=busca)
btn1.place(x=20, y=300, width=50, height=20)
janela.mainloop()