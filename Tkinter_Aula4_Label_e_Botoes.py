#*************************************************************************************************
#                           TRABALHANDO COM LABELS E BOTÕES
#*************************************************************************************************
#INCLUDES
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'
#FUNÇÕES
def clica_botao():                      #Função que será chamada quando apertar o botão
    print('Clicou no botão!')
    lb['text'] = 'Funcionou!'           #Altera a propriedade text do Label
#GUI
janela = Tk()
janela.geometry(resolucao)
bt = Button(janela, width=20, text='OK', command=clica_botao)       #Define um botão com tamanho 20
                                                                    # command é o evento de clicar
                                                                    # no botão e está ligado a função
                                                                    # clica_botao(). OBS.: Aqui o nome
                                                                    # da função não leva o ()
lb = Label(janela, text='Teste')
#Layout
bt.place(x=100,y=100)
lb.place(x=100,y=150)
janela.mainloop()

