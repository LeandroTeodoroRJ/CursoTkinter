#*************************************************************************************************
#                               GERENCIADOR DE LAYOUT PACK
#*************************************************************************************************
#O gerenciador de layout pack agrupa os widgets conforme determinadas propriedades
#INCLUDES
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'

#GUI
janela = Tk()
janela.geometry(resolucao)
bt1 = Button(janela, width=20, text='Botão 1')
bt2 = Button(janela, width=20, text='Botão 2')
bt3 = Button(janela, width=20, text='Botão 3')
bt4 = Button(janela, width=20, text='Botão 4')
#LAYOUT
#Definindo gerenciador de Layout pack, a ordem de agrupamento será a ordem da sequencia de cada
#linha de comando, no caso vem bt3-bt2-bt1-bt4
bt4.pack(side=TOP)      #Alinha o label 4 na parte superior da tela
bt3.pack(side=RIGHT)    #Alinha a direita. OBS: O valor da distância TOP é default.
bt2.pack(side=BOTTOM)   #Alinha abaixo.
bt1.pack(side=LEFT)     #Alinha a esquerda, a propriedade side pode ser: TOP BOTTOM LEFT RIGHT

janela.mainloop()
