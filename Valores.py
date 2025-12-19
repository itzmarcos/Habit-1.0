cont = soma = total = valor = 0
valor = int(input('Digite um valor: '))
while valor != 999:
    soma += valor
    cont += 1
    valor = int(input('Digite um valor: '))
    if valor == 999:
        print(f'Voce digitou {cont} numeros e a soma dos valores digitado é {soma}')