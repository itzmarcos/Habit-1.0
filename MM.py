maior = menor = cont = soma = media = 0
resposta = ''
while resposta != 'N':
    numero = int(input('Digite um valor: '))
    resposta = str(input('Voce deseja continua: ')).upper()
    cont += 1
    soma += numero
    media = soma // cont
    if cont == 1:
       maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    if resposta == 'N':
        print('Programa Finalizado...')

print(f'Voce digitou {cont} numeros e a media foi {media}')
print(f'O maior numero digitado foi {maior}, e o menor foi {menor}')