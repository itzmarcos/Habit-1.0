# VALORES

cont = soma = 0
while True:
    valor = int(input('Digite um valor: ')) 
    if valor == 0:
        break
    soma += valor
    cont += 1 
print(f'Voce digitou {cont} numeros e a soma dos valores digitado é {soma}')