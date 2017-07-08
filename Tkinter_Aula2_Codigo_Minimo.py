#*************************************************************************************************
#                                     O CÓDIGO MÍNIMO
#*************************************************************************************************

import tkinter as tk    #Importa a biblioteca tkinter e nomeia como tk

janela = tk.Tk()        #Instancia a variável janela como uma classe Tk
janela.title('Janela principal')    #Título superior da janela
janela['bg'] = 'green'              #Altera a cor de fundo da janela, algumas propriedades são
                                    #acessadas como se fossem um dicionário

#Configurações da janela
janela.geometry('800x300+100+100')  # 'LARGURAxALTURA+DISTÂNCIA_ESQUERDA+DISTÂNCIA_DO_TOPO'
                                    #passado em formato string. Medidas em pixels.
janela.geometry('800x300')          #As distâncias do topo e esquerda inicializadas como default

janela.mainloop()      #Abre a janela e interrompe o script enquanto a janela estiver sendo exibida





