# LENDO PESOS

maior = 0
menor = 0
for p in range(1, 5):
    peso = float(input(f'O peso da {p} é: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi {maior}')
print(f'O menor peeso lido foi {menor}')