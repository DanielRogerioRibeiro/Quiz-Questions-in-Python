# Janela Quiz

from tkinter import *

#Cores
cor1 ='#e6e6e6' #gray
cor2 ='#0dff00' #green

window = Tk()
window.title("QUESTÕES SOBRE PYTHON")
window.geometry('600x350') 
window.config(bg=cor1)
window.iconphoto(False, PhotoImage(file="Quiz Questions in Python/imagens/Python_logo.png"))
window.resizable(width=False,height=False)


title_1 = Label (window, width=50, text= '*****Seja Bem-Vindo ao Quiz Python*****', font=('Arial 15'), fg=cor2, bg='blue', pady=5)
title_1.place(x=20, y=0)

#title_2 = Label (window, width=60, text= "Para iniciar click no Nível que você deseja jogar:  ", font=('Arial 15'), fg='black')
#title_2.grid(row=1, column=2, padx=10)




window.mainloop()