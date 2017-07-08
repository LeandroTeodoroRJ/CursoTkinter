#*************************************************************************************************
#                                    INTRODUÇÃO AOS EVENTOS
#*************************************************************************************************
#INCLUDES
from functools import partial       #Include necessário para a função partial
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'
#FUNÇÕES
def clica_botao(botao):             #Função que é chamada quando os botões são clicados
    print('Clicou no botão!')
    if (botao == bt1):              #Identifica qual dos botões foi clicado
        print('Clicou no Botão 1')
    elif(botao == bt2):
        print('Clicou no Botão 2')

#GUI
janela = Tk()
janela.geometry(resolucao)
bt1 = Button(janela, width=20, text='Botão 1')
bt1['command'] = partial(clica_botao, bt1)      #Passa como parâmetro 'bt1' para a função clica_botao
bt2 = Button(janela, width=20, text='Botão 2')
bt2['command'] = partial(clica_botao, bt2)      #Passa como parâmetro 'bt2' para a função clica_botao

#Layout
bt1.place(x=100,y=100)
bt2.place(x=100,y=130)

janela.mainloop()
