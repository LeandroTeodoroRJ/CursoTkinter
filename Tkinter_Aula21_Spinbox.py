#*************************************************************************************************
#                                        SPINBOX
#*************************************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*

#CONSTANTES E DEFINIÇÕES
resolucao = '600x200+200+200'

#FUNÇÕES
def clica_botao():
    print(valor.get())      #Retorna a string contida no Spinbox

#GUI
janela = Tk()
janela.geometry(resolucao)
valor = StringVar()
Meu_Spinbox = Spinbox(janela, textvariable=valor, from_=0, to=10, increment=1, state='readonly')
bt1 = Button(janela, text='OK', command=clica_botao)
#Layout
Meu_Spinbox.grid(row=0, column=0, sticky=W)
bt1.grid(row=1, column=1, sticky=W)

janela.mainloop()

#Na linha 19
#A opção state='readonly' pode ser removida para escrita direta.
#A função valor.get() retorna o valor contido no Spinbox
#As opções from, to e increment são o valor inicial, valor final e o passo de incremento
#dos botões das setas respectivamente.
