#******************************************************************************************************
#                                           CRIANDO MENUS
#******************************************************************************************************

from tkinter import *
def donothing():                                        #Função de ação de escolha da opção
   print('Do nothing')


root = Tk()
menubar = Menu(root)                                    #Inicializa o container Menu na janela root
filemenu = Menu(menubar, tearoff=0)                     #Primeira coluna do Menu (filemenu)
menubar.add_cascade(label="File", menu=filemenu)        #Nome da primeira coluna do menu, propriedade label.
filemenu.add_command(label="New", command=donothing)    #Opções da primeira coluna do menu.
filemenu.add_command(label="Open", command=donothing)   #Command será a função chamada quando clica no na
                                                        #opção do menu.
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()                                #Insere um separador no menu na primeira coluna, entre
                                                        #as opções Save e Exit
filemenu.add_command(label="Exit", command=root.quit)   #root.quit fecha a janela

editmenu = Menu(menubar, tearoff=0)                     #Segunda coluna do Menu (editmenu)
menubar.add_cascade(label="Edit", menu=editmenu)        #Segunda coluna do Menu
editmenu.add_command(label="Undo", command=donothing)   #Opções da segunda coluna do menu
editmenu.add_separator()                                #Insere um separador na segunda coluna
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)

root.config(menu=menubar)                               #Carrega o menu na tela

root.mainloop()
