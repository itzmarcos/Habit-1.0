# ANÁLISE DE DADOS DO GRUPO


totald = homem = mulher = 0
c = 'S'
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]   
    if idade >= 18:
        totald += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continua: ')).strip().upper()[0]
    if c == 'N':
        break
print(f'O total de pessoas com mais de 18 anos: {totald} ')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos...')