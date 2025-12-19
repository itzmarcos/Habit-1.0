print('---------TABUADA---------')
while True:   
    valor = int(input('Quer ver a tabuada de qual valor: '))
    if valor <= 0:
        print('Programa Finalizando')
        break
    for c in range(1, 11):
        resultado = c * valor
        print(f'{valor} x {c} = {resultado}')


