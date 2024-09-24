'''
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''

#Cria uma função que gera a sequência até chegar ao valor de atribuido à "num"
def fib_sequencia(num):
    sequencia = [0, 1]
    while sequencia[-1] < num:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

#Verifica se o valor de "num" está na sequência
def pert_sequencia(num):
    sequencia = fib_sequencia(num)
    if num in sequencia:
        print("O número digitado pertence à sequência de Fibonacci.")
    else:
        print("O número digitado não pertence à sequência de Fibonacci.")
    return sequencia

#Pede para o usuário digitar um número (valor de "num")
numero = int(input("Informe um número: "))

#Exibe na tela o resultado
print(pert_sequencia(numero))