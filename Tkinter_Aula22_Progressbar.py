#*************************************************************************************************
#                                        PROGRESSBAR
#*************************************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*
from time import*

#CONSTANTES E DEFINIÇÕES
resolucao = '600x200+200+200'

#FUNÇÕES
def clica_botao():
    passo = 0
    while passo < 100:
        passo += 2
        BarraProgresso.step(2)          #Configura o proximo passo da barra, que vai de 2 em 2
        BarraProgresso.update()         #Atualiza a posição da barra
        sleep(0.1)                      #Tempo de delay de 0.2 segundos
        print(passo)


#GUI
janela = Tk()
janela.geometry(resolucao)
BarraProgresso = Progressbar(janela, orient=HORIZONTAL, length=200)  #Barra na posição horizontal
BarraProgresso.config(maximum=100)      #Configura o valor para barra completamente cheia
bt1 = Button(janela, text='Começar', command=clica_botao)
#Layout
BarraProgresso.grid(row=0, column=1, sticky=W)
bt1.grid(row=1, column=1)

janela.mainloop()
