#*************************************************************************************************
#                                    CHECK BUTTON
#*************************************************************************************************
#INCLUDES
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'
#FUNÇÕES
def clica_caixa():
    print(var_check.get())              #Imprime no console o estado do CheckButton, função get() na variável var_check
    if var_check.get()=='Ligado':       #Checa para saber se está ligado ou desligado.
        print('Está selecionado.')
    else:
        print('Não está selecionado.')

#GUI
janela = Tk()
janela.geometry(resolucao)
var_check = StringVar()
BT_check = Checkbutton(janela, width=20, text='Botão Check',
                       onvalue='Ligado', variable=var_check, offvalue='Desligado', command=clica_caixa)
#Layout
BT_check.place(x=100,y=100)

janela.mainloop()

#Na linha 20 as propriedades onvalue e offvalue são os parâmetros passados a variável var_check quando
#ocorre o evendo de marcar ou desmarcar a caixa. Esse evento chama a função clica_caixa(), referida
#na propriedade command.
