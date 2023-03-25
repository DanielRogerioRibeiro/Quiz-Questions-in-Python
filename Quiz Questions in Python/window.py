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

title_2 = Label (window, width=50, text= "Escolha uma Alternativa  ", font=('Arial 12'), fg='black')
title_2.place(x=70, y=60)

title_3 = Label (window, width=50, height=2 ,text= "Inserir a Pergunta  ", font=('Arial 15'), fg='black')
title_3.place(x=20, y=120)

score = Label (window, width=20, height=2 ,text= "Your Score = ", font=('Arial 10'), fg='black', anchor='w')
score.place(x=400, y=300)

#Botão
button_A = Button(window, width=35, height=1, text="A-) ", relief='raised', fg=cor2, bg='black')
button_A.place (x=20, y=200)

button_B = Button(window, width=35, height=1, text="B-) ", relief='raised', fg=cor2, bg='black')
button_B.place (x=20, y=250)

button_C = Button(window, width=35, height=1, text="C-) ", relief='raised', fg=cor2, bg='black')
button_C.place (x=300, y=200)

button_D = Button(window, width=35, height=1, text="D-) ", relief='raised', fg=cor2, bg='black')
button_D.place (x=300, y=250)

window.mainloop()