'''
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
'''

#Cria uma função para contar a quantidade de vogais 'a'
def cont_a(letra):

#Deixa as letra minúsculas
    letra=letra.lower()
#Conta e armazena o resultado em "cont"
    cont=letra.count('a')
    if cont >0:
        return f"Na palavra digitada a vogal 'a' aparece {cont} vezes"
    else:
        return "A vogal 'a' não foi encontrada na palavra digitada."
#O uso de return no lugar de print também é possivel como no exemplo acima.

#Pede ao usuário para escrever algo
palavra=str(input("Digite uma palavra ou uma frase: "))
#Exibe na tela o resultado
print(cont_a(palavra))