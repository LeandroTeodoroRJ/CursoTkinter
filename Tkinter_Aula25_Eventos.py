#*************************************************************************************************
#                                            EVENTOS
#*************************************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*
from time import*

#CONSTANTES E DEFINIÇÕES
resolucao = '600x200+200+200'

#FUNÇÕES
def apertou_tecla(event):                           #Função do evento de apertar a tecla
    print('Você apertou a tecla:', event.char)      #Retorna o tecla precionada
    print('O código da tecla é:', event.keycode)    #Retorna os códigos das teclas, inclusive
                                                    #as teclas de função.
def botao_direito(event):                           #O parâmetro event deve ser passado obrigatoriamente
    print('Você apertou o botão direito do mouse')
def on_leave(event):
    print('Você retirou o mouse do botão')
def on_enter(enter):
    print('Você está com o mouse em cima do botão')


#GUI
janela = Tk()
janela.geometry(resolucao)
janela.bind('<Key>', apertou_tecla)         #<Key> é o evento de precionar a tecla e chama a rotina
                                            #que tratará esse evento apertou_tecla()
janela.bind('<Button-3>', botao_direito)    #Evento do botão direito do mouse
lb1 = Label(janela, text='1) Aperte uma tecla e observe o console.')
lb2 = Label(janela, text='2) Aperte o botão direito do mouse.')
bt1 = Button(janela, text='3) Deixe o mouse sobre o botão e depois retire', width=50)
bt1.bind('<Leave>', on_leave)               #Os eventos estão disponíveis também para os outros objetos
bt1.bind('<Enter>', on_enter)               #Evento de colocar o ponteiro do mouse sobre o objeto

#Layout
lb1.grid(row=0, column=0, sticky=W)
lb2.grid(row=1, column=0, sticky=W)
bt1.grid(row=2, column=0, sticky=W)

janela.mainloop()

#Muitos mais eventos estão disponíveis em: http://www.python-course.eu/tkinter_events_binds.php
