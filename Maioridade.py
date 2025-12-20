from datetime import datetime
atual = datetime.now().year

maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c} pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 18:  
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E tivemos {menor} pessoas menores de idade')