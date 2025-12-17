soma = 0


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print("""
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NUMEROS
        [5] SAIR DO PROGRAMA 
""")
    
    opcao = int(input('Qual sua opcao: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é {soma}!')
    elif opcao == 2:
        mult = n1 * n2
        print(f'A multiplicacao dos numero {n1} x {n2} é {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O {n1} é maior que {n2}!')
        else:
                print(f'O {n2} é maior que {n1}!')
    if opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if opcao == 5:
        print('Finalizando o programa...')