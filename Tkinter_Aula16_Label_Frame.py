#*************************************************************************************************
#                                          LABEL FRAME
#*************************************************************************************************
#INCLUDES
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'
#FUNÇÕES
def clica_botao():
    print('Clicou no botão!')
    lb['text'] = 'Funcionou!'           #Altera a propriedade text do Label

#GUI
janela = Tk()
janela.geometry(resolucao)
lb = Label(janela, text='Teste')
frame1 = LabelFrame(janela, width=60, height=60, text='Frame 1', bd=2) #bd = valor da borda em pixels
bt = Button(frame1, text='OK', command=clica_botao)
#Layout
frame1.grid(row=0, column=0)
lb.grid(row=2, column=0)
bt.grid(row=1, column=0)

janela.mainloop()

#LabelFrame é um container, pode receber outros widgets. Assim facilitando a organização em blocos
#de widgets, esses blocos podem ser nomeados pela propriedade text do LabelFrame.
