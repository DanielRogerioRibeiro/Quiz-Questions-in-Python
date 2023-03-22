# Quiz sobre Python
# Este quiz tem como objetivo apresentar uma série de perguntas sobre Python para que o usuário responda

print ("*****Seja Bem-Vindo ao Quiz Python*****")
print ("*****Para iniciar por favor selecione o tema:")
tema_int = input("(1) Operadores (2) Cálculo (3) Sintaxe : ")
tema = int(tema_int)

if (tema == 1):
    print ("Ok...Vamos as Operações")

elif (tema == 2):
    print ("Ok...Vamos aos Cálculos")

else:
    print ("Ok...Vamos as Sintaxes")

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

for question, answer in questions.items():
        user_answer = input(question)
        if user_answer.lower() == answer.lower():
            print("Resposta correta!")

        else:
            print("Resposta incorreta.")

