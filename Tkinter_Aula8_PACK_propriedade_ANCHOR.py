#*************************************************************************************************
#                        GERENCIADOR DE LAYOUT PACK - PROPRIEDADE ANCHOR
#*************************************************************************************************
#INCLUDES
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'

#GUI
janela = Tk()
janela.geometry(resolucao)
bt1 = Button(janela, width=5, text='Botão 1')
bt2 = Button(janela, width=5, text='Botão 2')
bt3 = Button(janela, width=5, text='Botão 3')
bt4 = Button(janela, width=5, text='Botão 4')
#LAYOUT
#Definindo gerenciador de Layout pack, a ordem de agrupamento será a ordem da sequencia de cada
#linha de comando, no caso vem bt3-bt2-bt1-bt4
bt3.pack(side=LEFT, anchor=N)
bt2.pack(side=LEFT, anchor=N)
bt1.pack(side=LEFT, anchor=S)
bt4.pack(side=LEFT, anchor=E)

janela.mainloop()

#A propriedade anchor alinha os componentes, pode receber os valores:
# CENTER
# N - Norte
# S - Sul
# W - Oeste
# E - Leste, e suas componentes:
# NW - NE - SE - SW
