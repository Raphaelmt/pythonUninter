print('Bem-vindo(a) a Sorveteria de Raphael Mendes Toso')
print(38*'-'+'Cardápio'+38*'-')
print('| N° DE BOLAS  | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|      1       |         R$ 6,00        |      R$ 7,00       |       R$ 8,00       |')
print('|      2       |         R$ 11,00       |      R$ 13,00      |       R$ 15,00      |')
print('|      3       |         R$ 15,00       |      R$ 18,00      |       R$ 21,00      |')
print(84*'-')

# Inicia o valor total fora do while
valorTotal = 0
while True:
    # Entra com o sabor, em caso de sabor inválido, pede o sabor novamente
    sabor = input('Entre com o sabor desejado (tr/es/pr):')
    if sabor != 'tr' and sabor != 'es' and sabor != 'pr':
        print('Sabor inválido. Tente novamente.')
        continue

    # Entra com a quantidade, em caso de quantidade inválida, pede o sabor novamente
    quantidade = input('Entre com o número de bolas de sorvete desejado (1/2/3):')
    if quantidade != '1' and quantidade != '2' and quantidade != '3':
        print('Número de bolas de sorvete inválido. Tente novamente.')
        continue

    # Após validadr as entradas, calcula o valor do pedido
    # Aproveita o if para criar uma variável para exibição do sabor
    if sabor == 'tr':
        saborPrint = 'TRADICIONAL'
        if quantidade == '1':
            valorPedido = 6.00
        elif quantidade == '2':
            valorPedido = 11.00
        else:
            valorPedido = 15.00
    elif sabor == 'pr':
        saborPrint = 'PREMIUM'
        if quantidade == '1':
            valorPedido = 7.00
        elif quantidade == '2':
            valorPedido = 13.00
        else:
            valorPedido = 18.00
    else:
        saborPrint = 'ESPECIAL'
        if quantidade == '1':
            valorPedido = 8.00
        elif quantidade == '2':
            valorPedido = 15.00
        else:
            valorPedido = 21.00

    # Adiciona o valor do pedido ao total
    valorTotal += valorPedido
    # Exibe o pedido para o usuário
    print('Você pediu {} bola de sorvete no sabor {}: R$ {:.2f}'.format(quantidade, saborPrint, valorPedido))
    # Verifica se o cliente quer pedir mais
    op = input('Deseja mais algum sorvete?(s/digite outra tecla):')
    if op != 's':
        break

print('O valor total a ser pago: R$ {:.2f}'.format(valorTotal))
