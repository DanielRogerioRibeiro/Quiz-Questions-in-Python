# Quiz sobre Python
# Este quiz tem como objetivo apresentar uma série de perguntas sobre Python para que o usuário responda

print ("*****Seja Bem-Vindo ao Quiz Python*****")



# Lista de perguntas e respostas
questions = {
    "Qual é o operador de atribuição em Python? ": "=",
    "Qual é o operador para concatenar duas strings em Python? ": "+",
    "Qual é o resultado da expressão 2 + 2 * 3? ": "8",
    "Qual é a função para imprimir algo na tela em Python? ": "print",
    "Qual é o método para adicionar um elemento a uma lista em Python? ": "append",
    "Qual é a função usada para ler a entrada do usuário?": "input",
    "Qual é a sintaxe para definir uma função em Python?": "def nome_da_funcao():"
}

#Função para executar o Quiz
def run_quiz(questions):
    score = 0
 
#Inicio do quiz
    for question, answer in questions.items():
        user_answer = input(question)
        if user_answer.lower() == answer.lower():
            print("Resposta correta!")
            score += 1
        else:
            print("Resposta incorreta.")
        
        print(f"Você acertou {score} de {len(questions)} perguntas.")

# Executa o quiz
run_quiz(questions)
