#*************************************************************************************************
#                                         LISTBOX
#*************************************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*        #Biblioteca necessária

#CONSTANTES E DEFINIÇÕES
resolucao = '600x200+200+200'
#Lista que será carregada
Texto = ['Brasil', 'Argentina', 'Venezuela', 'Uruguai', 'Paraguai', 'Colombia', 'Equador']

#FUNÇÕES
def clica_botao():
    index = Caixa_Lista.curselection()  #Retorna o index relativo a opção seleciodada
    if index != ():                     #Checa para saber se o usuário selecionou algum item
        print(index)                    #Imprime o index
        print(Caixa_Lista.get(index))   #Imprime a opção selecionada

#GUI
janela = Tk()
janela.geometry(resolucao)
BarraRolagem = Scrollbar(janela, orient=VERTICAL)    #Define a orientação da barra de rolagem
Caixa_Lista = Listbox(janela, selectmode=SINGLE, width=20, height=5, yscrollcommand=BarraRolagem.set)
BarraRolagem.config(command=Caixa_Lista.yview)       #Rola o texto com o click
for item in Texto:
    Caixa_Lista.insert('end', item)                  #Insere uma lista no ListBox item a item
bt1 = Button(janela, text='Seleciona', command=clica_botao)
#Layout
Caixa_Lista.grid(row=0, column=0, sticky=W)
BarraRolagem.grid(row=0, column=1, sticky=(N,S))
bt1.grid(row=1, column=0, sticky=N)

janela.mainloop()
