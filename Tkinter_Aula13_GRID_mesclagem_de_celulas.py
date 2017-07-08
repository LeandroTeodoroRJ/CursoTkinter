#*************************************************************************************************
#                        GERENCIADOR DE LAYOUT GRID - MESCLAGEM DE CÉLULAS
#*************************************************************************************************
#INCLUDES
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'

#GUI
janela = Tk()
janela.geometry(resolucao)
bt1 = Button(janela, width=15, text='Botão 1')
bt2 = Button(janela, width=5, text='Botão 2')
bt3 = Button(janela, width=5, text='Botão 3')
bt4 = Button(janela, width=5, text='Botão 4')
#layout
bt1.grid(row=1, column=1)                           #O tamanho da coluna é dada pelo tamanho do botão 1
bt2.grid(row=1, column=2)
bt3.grid(row=2, column=1, sticky=W+E, columnspan=2) #Mescla a coluna 1 com a 2 e ocupa toda área de Oeste a Leste
bt4.grid(row=1, column=3, sticky=N+S, rowspan=2)    #Mescla a linha 1 com a 2 e ocupa toda área de Norte a Sul

janela.mainloop()

# A propriedade rowspan mescla as linhas e a propriedade colunspan mescla as culunas
