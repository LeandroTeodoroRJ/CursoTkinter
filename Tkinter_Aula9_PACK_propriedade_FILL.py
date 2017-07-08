#*************************************************************************************************
#                        GERENCIADOR DE LAYOUT PACK - PROPRIEDADE FILL
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
#Layout
bt3.pack(side=TOP, fill=X)      #Expande no eixo X
bt2.pack(side=LEFT, fill=Y)     #Expande no eixo Y
bt1.pack(side=LEFT, anchor=S)
bt4.pack(side=LEFT, anchor=S)

janela.mainloop()

#A propriedade FILL faz o widget ocupar toda a área na qual foi definida
