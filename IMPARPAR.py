from random import randint
soma = cont = 0

v = 0
d = 0
while True:
    jogador = int(input('Escolha um numero: '))
    computador = randint(0, 10)
    soma = computador + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar: ')).strip().upper()[0]
    print(f'Voce escolheu {jogador} e o computador {computador}. Total foi {soma}')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            d += 1
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Voce VENCEU!')
        else:
            print('Voce PERDEU!')
            d += 1
            break
    print('Vamos joga novamente!')
print(f'Fim de jogo! Voce venceu {v} vezes e perdeu {d} vezes')