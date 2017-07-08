#*************************************************************************************************
#                        GERENCIADOR DE LAYOUT GRID - PROPRIEDADE STICKY
#*************************************************************************************************
#INCLUDES
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'

#GUI
janela = Tk()
janela.geometry(resolucao)
bt1 = Button(janela, width=15, text='Botão 1') #Define o tamanho 3 vezes maior que os outros botões
bt2 = Button(janela, width=5, text='Botão 2')
bt3 = Button(janela, width=5, text='Botão 3')
bt4 = Button(janela, width=5, text='Botão 4')
#Layout
bt1.grid(row=0, column=0)               #O tamanho da coluna é dada pelo tamanho do botão 1
bt2.grid(row=0, column=1)
bt3.grid(row=1, column=0, sticky=N)     #Alinha ao Norte da célula
bt4.grid(row=2, column=0, sticky=E)     #Alinha ao Leste da célula

janela.mainloop()

#A propriedade sticky alinha os componentes dentro da célula, pode receber:
# N - Norte
# S - Sul
# W - Oeste
# E - Leste, e suas componentes
# NW - NE - SE - SW
