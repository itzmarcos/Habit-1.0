# CAIXA DE LOJA

total = valor = menor = cont = 0
barato = ' '
print('--------------CAIXA---------------')
while True: 
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    total += preco
    if preco >= 1000:
        valor += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
        
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-----------Conta Finalizada------------')
print(f'O total da compra foi de R${total} reais')
print(f'Temos {valor} produtos custando mais de R$1000.00 reais!')
print(f'O produto mais barato foi {barato} que custou {menor} reais')