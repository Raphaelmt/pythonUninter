def cachorro_peso():
    while True:
        try:
            peso = float(input('Entre com o peso do cachorro:'))
        # Verifica se o valor é numérico
        except ValueError:
            print('Por favor entre com o peso do cachorro novamente.')
            continue
        # Verifica o peso e retorna o valor base
        if peso < 3:
            return 40.0
        elif 3 <= peso < 10:
            return 50.0
        elif 10 <= peso < 30:
            return 60.0
        elif 30 <= peso < 50:
            return 70.0
        # Se o peso for maior que 50, exibe mensagem e reoete a pergunta
        else:
            print('Não aceitamos cachorros tão grandes.')
            continue


def cachorro_pelo():
    while True:
        print('Entre com o pelo do cachorro \n'
              'c - Pelo Curto \n'
              'm - Pelo Médio \n'
              'l - Pelo Longo')
        pelo = input()
        # Verifica se a opção de pelo é válida
        if pelo != 'c' and pelo != 'm' and pelo != 'l':
            print('Opção inválida.')
            continue

        # Retorna o multiplicador correto para o tipo de pelo
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        else:
            return 2


def cachorro_extra():
    soma_extra = 0
    while True:
        print('Deseja adicionar mais algum serviço? \n'
              '1 - Corte de Unhas - R$ 10,00 \n'
              '2 - Escovar Dentes - R$ 12,00 \n'
              '3 - Limpeza de Orelhas - R$ 15,00 \n'
              '0 - Não desejo mais nada')
        adicional = input()
        # Dependendo da opçao digitada, adiciona ao valor extra
        if adicional == '1':
            soma_extra += 10.0
        elif adicional == '2':
            soma_extra += 12.0
        elif adicional == '3':
            soma_extra += 15.0
        # Ao digitar 0 retorna o valor extra
        elif adicional == '0':
            return soma_extra
        # Ao digitar outra coisa, repete a pergunta
        else:
            print('Opção inválida;')
            continue


print('Bem-vindo(a) ao Pet Shop de Raphael Mendes Toso')
# Chama as funções para obter os valores
base = cachorro_peso()
mult = cachorro_pelo()
extra = cachorro_extra()
total = base * mult + extra
print('Total a pagar(R$): {} (peso: {} * pelo: {} + adicional(is): {}'.format(total, base, mult, extra))
