#*************************************************************************************************
#                               GERENCIADORES DE LAYOUT  - PLACE
#*************************************************************************************************

from tkinter import*

janela = Tk()
janela.geometry('300x300+200+200')

lb = Label(janela, text='Fala galera!')     #O label estará contido na variável janela conforme o primeiro
                                            #parâmetro passado. Atribui a intância do Label para uma variável
                                            #de nome lb
lb.place(x=100, y=100)                      #Gerenciador de Layout Place:
                                            #As coordenadas do label são (100,100) do canto superior
                                            #esquerdo da tela (x, y)


janela.mainloop()
