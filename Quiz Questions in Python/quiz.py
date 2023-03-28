# Quiz sobre Python
# Este quiz tem como objetivo apresentar uma série de perguntas sobre Python para que o usuário responda
from tkinter import *
import random

#Cores
cor1 ='#dfe0e8' #gray
cor2 ='#0dff00' #green
cor3 ='#3852d1' #blue
cor4 ='#050505' #black

# Cria uma window
window = Tk()
window.title ("QUESTÕES SOBRE PYTHON")
window.geometry ('600x350') 
window.iconphoto (False, PhotoImage(file="imagens/Python_logo.png"))
window.resizable (width=False,height=False)

img = PhotoImage (file="imagens/Python_logo.png")

Label.logo = Label(window, image=img, anchor='center').pack()

# Cria uma label para exibibição
title_1 = Label (window, width=50, text= '*****Seja Bem-Vindo ao Quiz Python*****', font=('Arial 15'), fg=cor2, bg='blue', pady=5)
title_1.place(x=20, y=0)

title2_question = Label(window, width=50, height=2 , text="", font=('Arial 15'), fg='black')
title2_question.place(x=20, y=120)

# Cria uma entrada de texto para o usuário digitar a resposta
input_answer = Entry(window, font=('Arial 15'), bg=cor1, fg=cor4)
input_answer.place (x=180, y=200)


# Lista de perguntas e respostas
questions_answer = {
    "Qual é o operador de atribuição em Python? ": "=",
    "Qual é o operador para concatenar duas strings em Python? ": "+",
    "Como se chama o método que adiciona um elemento\nao final de uma lista em Python?": "append",
    "Qual é o resultado da expressão 2 + 2 * 3? ": "8",
    "Qual é o nome da função para imprimir algo na\ntela em Python? ": "print" or "Print" or "PRINT",
    "Qual é a função usada para ler a entrada do usuário?": "input",
    "Qual é a sintaxe para definir uma função em Python?": "def nome_da_funcao():"
}

# Lista com as perguntas do Quiz
questions = list(questions_answer.keys())

# Função para verificar a resposta do usuário
def confirm_answer():
    answer_usuario = input_answer.get()
    answer_correct = questions_answer[title2_question["text"]]
    
    if answer_usuario == answer_correct:
        label_answer = Label(window, text="Resposta correta!", font=("Arial", 14), fg="green")
        
    else:
        label_answer = Label(window, width=30, height=1, text="A Resposta Correta era: {}" .format(answer_correct), font=("Arial", 14), fg="red", bg=None)
        
    
    label_answer.place (x=150, y=250)
    next_question()
    

# Cria um botão para o usuário confirmar sua resposta
button_confirm = Button(window, text="Next", font=("Arial", 14),  command=confirm_answer)
button_confirm.place (x=520, y=300)

# Função para escolher a próxima pergunta
def next_question():
    # Escolhe uma pergunta aleatoriamente
    question = random.choice(questions)
    
    # Remove a pergunta da lista de perguntas para não repetir
    questions.remove(question)
    
    # Define o texto da label para exibir a pergunta
    title2_question["text"] = question
    
    # Limpa a entrada de texto
    input_answer.delete(0, END)

    
    # Se todas as perguntas já foram respondidas, exibe mensagem final
    if not questions:
        title2_question["text"] = "Fim do Quiz!"
        #input_answer.pack_forget()
        #button_confirm.pack_forget()

# Chama a função para escolher a primeira pergunta
next_question()


#Criando função sair
def exit():
    window.destroy()
    return


# Cria um botão sair
button_exit = Button(window, text="Exit", font=("Arial", 14),  command=exit)
button_exit.place (x=20, y=300)

window.mainloop()
