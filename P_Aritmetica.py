# p = int(input('Primeiro termo: '))
# r = int(input('Razão da PA: '))
# termo = p
# cont = 1
# while cont <= 10:
#     print(f'{termo} -> ', end='')
#     termo += r
#     cont += 1
# print('END')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}')
        termo += razao
        cont += 1
    mais = int(input('Quantos termo voce quer a mais: '))

print(f'Finalizando com o total de {total} termos mostrado')