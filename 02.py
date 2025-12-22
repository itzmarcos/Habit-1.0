# ANALISADOR

somaidade = mediaidade = maioridadem = nomevelho = totmulher20 = 0

for p in range(1, 5):
    print(f'-------{p} PESSOA -------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: M/F: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadem:
        maioridadem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade:.1f} anos')
print(f'O homem mais velho tem {maioridadem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulher com menos de 20 anos')