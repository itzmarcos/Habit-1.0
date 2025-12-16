from random import randint
# resposta = tentativas = 0
computador = randint(1, 10)
# print('Sou o seu computador...')
# print('Acabei de pensar em um numero entre 0 e 10')
# print('Será que voce consegue adivinha qual foi?')
# while resposta != computador:
#     resposta = int(input('Qual sua resposta: '))
#     tentativas += 1
#     if resposta == computador:
#         print(f'Voce acertou em {tentativas} tentativas.. ')
#     else:
#         print('Tente novamente!')


print('Sou o seu computador...')
print('Acabei de pensar em um numero entre 0 e 10')
print('Será que voce consegue adivinha qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos.. Tente mais uma vez')
print(f'Acertou com {palpites} tentativas. Parabéns!')