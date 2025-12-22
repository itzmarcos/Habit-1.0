# VALIDAÇÃO

sexo = str(input('Informe seu sexo: '))
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Digite novamente: '))
print(f'Sexo {sexo} registrado com sucesso!')