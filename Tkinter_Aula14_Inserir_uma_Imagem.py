#*************************************************************************************************
#                              INSERIR UMA IMAGEM NA TELA
#*************************************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*

#GUI
janela = Tk()
janela.geometry('600x300+200+200')
path = r'C:/DADOS/Informatica/Info_projetos/Python/Curso_de_Python/Anexos/logo.gif'  #Row string
global Minha_Imagem
Minha_Imagem = PhotoImage(file = path)      #Instancia como um objeto tipo PhotoImage
lb = Label(janela, image = Minha_Imagem)    #Carrega a imagem no label, também pode ser inserido
                                            #em um objeto tipo Button
#Layout
lb.place(x=100, y=100)

janela.mainloop()

#Uma Row String é uma string que será utilizada no formato que foi definida.
#Assim, desconsidera-se o caractere especial "/"
#Nem todos os formatos de imagem são aceitos.
