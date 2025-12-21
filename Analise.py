cont = soma = totald = menorv = homem = mulher = 0
c = 'S'
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    c = str(input('Quer continua: ')).strip().upper()[0]
    cont += 1
    if idade >= 18:
        totald += 1
    if sexo == 'M':
        homem += 1
    else:
        mulher += 1
    if c == 'N':
        break
print(f'O total de pessoas com mais de 18 anos: {totald} ')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de ...')