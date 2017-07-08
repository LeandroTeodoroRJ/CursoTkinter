#*************************************************************************************************
#                                    ABRIR UMA NOVA JANELA
#*************************************************************************************************
#INCLUDES
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'
#FUNÇÕES
def clica_botao():
    #GUI Janela 2
    janela2 = Tk()
    janela2.geometry(resolucao)         #Abre uma nova janela
    bt2 = Button(janela2, width=20, text='Fechar Janela', command=janela2.destroy) #Fecha a janela
    #Layout
    bt2.place(x=100,y=100)

    print('A janela foi aberta.')

#GUI
janela = Tk()
janela.geometry(resolucao)
bt = Button(janela, width=20, text='OK', command=clica_botao)
lb = Label(janela, text='Teste')
#Layout
bt.place(x=100,y=100)
lb.place(x=100,y=150)

janela.mainloop()
