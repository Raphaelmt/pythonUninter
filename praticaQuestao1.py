print('Bem-vindo a Loja do Raphael Mendes Toso')

# Entrada de dados
valorUnidade = float(input('Entre com o valor do produto:'))
quantidade = int(input('Entre com a quantidade do produto:'))
# Cálculo do valor sem desconto
valorTotal = valorUnidade * quantidade

# Se quantidade for menor que 200 o desconto será de 0%
if quantidade < 200:
    desconto = 0
# Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%
elif 200 <= quantidade < 1000:
    desconto = 0.05
# Se quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%
elif 1000 <= quantidade < 2000:
    desconto = 0.1
# Se quantidade for igual ou maior que 2000 o desconto será de 15%
else:
    desconto = 0.15

# Saída sem desconto
print('O valor SEM desconto : R$ {:.2f}'.format(valorTotal))
# Saída com desconto, se houver
if desconto > 0:
    print('O valor COM desconto : R$ {:.2f}'.format(valorTotal - valorTotal * desconto))
