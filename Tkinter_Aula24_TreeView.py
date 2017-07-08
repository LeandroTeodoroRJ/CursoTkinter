#*************************************************************************************************
#                                            TREEVIEW
#*************************************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*        #Biblioteca necessária

#CONSTANTES E DEFINIÇÕES
resolucao = '600x300+200+200'
#Lista que será carregada
Texto = [['Fabiana', '1.56', '60'],['Jaqueline', '1.70', '65'],['Juliana', '1.63', '64']]

#FUNÇÕES
def clica_botao():
    index = Tabela.selection()          #Retorna o index relativo a seleção
    print(type(index))                  #Imprime o tipo do objeto index
    if index != '':                     #Checa para saber se o usuário selecionou algum item
        print(index)                    #Imprime o formato do index
        Dicionario = Tabela.item(index)
        print(Dicionario)               #Retorna a estrutura do dicionário
        print(Dicionario['values'])     #Manipula o dicionário para retornar somente os valores
def deletar_registro():
    index = Tabela.selection()
    if index != '':                     #Checa para saber se o usuário selecionou algum item
       Tabela.delete(index)             #Deleta o item selecionado

#GUI
janela = Tk()
janela.geometry(resolucao)
BarraRolagem = Scrollbar(janela, orient=VERTICAL)   #Define a orientação da barra de rolagem
Tabela_Colunas = ('Nome', 'Altura', 'Peso')         #Define os nomes das colunas, que serão 3
Tabela = Treeview(janela, columns=Tabela_Colunas, show='headings', yscrollcommand=BarraRolagem.set)
Tabela.heading(0, text='Nome')                      #Configura os cabeçalhos
Tabela.heading(1, text='Altura')
Tabela.heading(2, text='Peso')
Tabela.column(0, width='100')                       #Configura a largura da coluna
Tabela.column(1, width='50')
Tabela.column(2, width='50')
for item in Texto:
    Tabela.insert('', 'end', values=item)           #Insere a lista no TreeView 3 colunas por vez
BarraRolagem.config(command=Tabela.yview)           #Rola o texto com o click
bt1 = Button(janela, text='Seleciona', command=clica_botao)
bt2 = Button(janela, text='Deletar', command=deletar_registro)

#Layout
Tabela.grid(row=0, column=0, sticky=W)
BarraRolagem.grid(row=0, column=1, sticky=(N,S))
bt1.grid(row=0, column=2, sticky=N)
bt2.grid(row=0, column=3, sticky=N)

janela.mainloop()

#Na linha 32 com a propriedade show='headings' os cabeçalhos serão mostrados na tabela. A barra de
#rolagem está configurada para a posição horizontal.
