#*************************************************************************************************
#                                      TKINTER - HELLO WORLD
#*************************************************************************************************

from tkinter import *

janela = Tk()       #Define janela como uma Tkinter Window que será a janela principal
Label(janela, text='Fala galera!').pack()   #Define um label com o gerenciador de layout pack
janela.mainloop()   #Abre a janela no programa

