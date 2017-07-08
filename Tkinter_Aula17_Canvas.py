#*************************************************************************************************
#                                           CANVAS
#*************************************************************************************************
#INCLUDES
from tkinter import*
#CONSTANTES E DEFINIÇÕES
resolucao = '500x500+200+200'

#GUI
janela = Tk()
janela.geometry(resolucao)
lb = Label(janela, text='Desenhando com Canvas')

Desenho = Canvas(janela, width=400, height=400, borderwidth=1, relief=RAISED)
#Área disponível para desenho início(0,0) e final(400,400). Com a opção RAISED a área
#fica em alto relevo

Desenho.create_line(0, 0, 200, 400, width=1)    #Linha - Ponto de início(0,0) e final(200,400)

p1 = (200,0)
p2 = (300,100)
p3 = (100,300)
Desenho.create_polygon(p1, p2, p3, width=1, outline='red', fill='')
#Cria um polígono com os pontos p1, p2 e p3. A opção outline recebe a cor da linha e fill recebe
#a cor do preenchimento interno (' ' para ficar transparente)

Desenho.create_oval(200, 200, 50, 50, width=4, fill='blue')
#Tendo um círculo inscrito num polígono e sendo o ponto superior esquerdo (x0,y0) e o ponto
#inferior direito (x1,y1), o círculo inscrito nesse polígono é dado pela função
#create_oval(x0, y0, x1, y1, opções...)

coord = (201, 201, 300, 300)
Desenho.create_arc(coord, start=360, extent=270, width=2, fill="blue")
#Para criar um arco, as coordenadas seguem a idéia do círculo, sendo que o ângulo do arco fica
#por conta as opções start e extent.

#Layout
lb.grid(row=0, column=0)
Desenho.grid(row=1, column=0)
janela.mainloop()
