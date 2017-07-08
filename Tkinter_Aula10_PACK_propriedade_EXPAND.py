#*************************************************************************************************
#                        GERENCIADOR DE LAYOUT PACK - PROPRIEDADE EXPAND
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
bt3.pack(side=TOP, fill=BOTH, expand=True)
bt2.pack(side=TOP, fill=BOTH, expand=True)
bt1.pack(side=TOP, fill=BOTH, expand=True)
bt4.pack(side=TOP, fill=BOTH, expand=True)

janela.mainloop()

#A propriedade expand divide igualmente o tamanho dos widgets de
#acordo com o espaço disponível disponível na janela que estão contidos.
