#*************************************************************************************************
#                                       COMBO BOX
#*************************************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*        #Biblioteca necessária

#CONSTANTES E DEFINIÇÕES
resolucao = '600x200+200+200'
#FUNÇÕES
def clica_botao():
    lb1['text'] = var_check.get()

#GUI
janela = Tk()
janela.geometry(resolucao)
var_check = StringVar()
opcoes_combo = ['Opção 1','Opção 2','Opção 3']
meu_combo = Combobox(janela, values=opcoes_combo, textvariable=var_check, state='readonly')
meu_combo.current(0)        #Define a primeira opção como default
#meu_combo.bind("<<ComboboxSelected>>", clica_botao())     #Evento para quando o combo box estiver selecionado
lb1 = Label(janela, text='Sua opção vai aparecer aqui!')
bt1 = Button(janela, text='OK', command=clica_botao)
#Layout
meu_combo.grid(row=0, column=0)
lb1.grid(row=0, column=1)
bt1.grid(row=1, column=1, sticky=W)
janela.mainloop()

#Na linha 19 a propriedade values é carregada com a lista definida em opcoes_combo, o valor selecionado
#pelo usuário é transferido para a variável var_check definida como StringVar() na linha 17, que será
#retornada na linha 12 pela função get().
#A linha 21 é uma exemplo de evento para o Combobox.
