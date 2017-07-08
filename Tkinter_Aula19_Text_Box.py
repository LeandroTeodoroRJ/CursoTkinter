#*************************************************************************************************
#                                      TEXT BOX
#*************************************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*        #Biblioteca necessária

#CONSTANTES E DEFINIÇÕES
resolucao = '600x200+200+200'
Texto = 'Essa mensagem vai \naparecer na caixa.'    #Texto que será carregado

#FUNÇÕES
def clica_botao():
    print(Caixa_de_texto.get(1.0,END))              #Retorna a string contida na caixa de texto

#GUI
janela = Tk()
janela.geometry(resolucao)
BarraRolagem = Scrollbar(janela, orient=VERTICAL)   #Define a orientação vertical para a barra de rolagem
Caixa_de_texto = Text(janela, wrap=WORD, width=20, height=5, yscrollcommand=BarraRolagem.set)
BarraRolagem.config(command=Caixa_de_texto.yview)   #Define que a barra de rolagem será anexada
                                                    #ao objeto Caixa_de_texto (text).
Caixa_de_texto.insert(INSERT, Texto)                #Insere a string na caixa de texto
bt1 = Button(janela, text='OK', command=clica_botao)
#Layout
Caixa_de_texto.grid(row=0, column=0, sticky=W)
BarraRolagem.grid(row=0, column=1, sticky=(N,S))
bt1.grid(row=1, column=0, sticky=N)

janela.mainloop()
