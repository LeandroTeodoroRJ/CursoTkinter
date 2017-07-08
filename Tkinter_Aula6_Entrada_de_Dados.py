#*************************************************************************************************
#                             ENTRADA DE DADOS - WIDGET ENTRY
#*************************************************************************************************
#INCLUDES
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+300+300'
#FUNÇÕES
def clica_botao():
    print(ed1.get())                    #Imprime no console o que tem dentro de ed1: função get()
    lb1['text'] = ed1.get()             #Altera a propriedade text do label
    if str(ed1.get()).isnumeric():      #Identifica se o valor digitado é puramente numérico
    #if str(ed1.get()).isalnum():       #Teste para outros valores numéricos que inclui o formato float
        print('O valor digitado é puramente numérico')
        num = int(ed1.get()) + 55       #Converte o valor digitado no edit para inteiro
    #   num = float(ed1.get()) + 55     #Converte o valor digitado no edit para float
        print('A soma do valor com 55 é: ', num)

#GUI
janela = Tk()
janela.geometry(resolucao)
ed1 = Entry(janela)
bt1 = Button(janela, width=20, text='OK', command=clica_botao)
lb1 = Label(janela, text='Label')
#Layout
ed1.place(x=100, y=100)
bt1.place(x=100,y=130)
lb1.place(x=100, y=160)

janela.mainloop()

#As linhas 13 e 16 são uma saída para utilização do programa com variáveis tipo float
