#*************************************************************************************************
#                                 GERENCIADOR DE LAYOUT GRID
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
#layout
bt1.grid(row=0, column=0)       # row = linha , column = coluna. Componente na linha 0 coluna 0
bt2.grid(row=1, column=0)
bt3.grid(row=2, column=2)
bt4.grid(row=3, column=3)

janela.mainloop()

#O gerenciador de Layout Grid divide a tela em linhas e colunas, onde cada elemento está
#localizado dentro de um endereço formado pelo par linha-coluna.
