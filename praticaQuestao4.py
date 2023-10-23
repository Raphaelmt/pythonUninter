def cadastrar_colaborador(id):
    print(73 * '*')
    print(23 * '-' + ' MENU CADASTRAR COLABORADOR ' + 22 * '-')
    # id vem da variável global
    print('id do colaborador {}'.format(id))
    # Entra com os dados e verifica se o usuário digitou um número
    nome = input('Por favor entre com o nome:')
    setor = input('Por favor entre com o setor:')
    while True:
        try:
            pagamento = float(input('Por favor entre com o pagamento (R$):'))
        except ValueError:
            print('Valor de pagamento inválido.')
            continue
        break
    # adiciona o colaborador como dicionário no final da lista
    global lista_colaboradores
    lista_colaboradores.append({'id': id, 'nome': nome, 'setor': setor, 'pagamento': pagamento})


def consultar_colaborador():
    while True:
        print(73 * '*')
        print(23 * '-' + ' MENU CONSULTAR COLABORADOR ' + 22 * '-')
        print('Escolha a opção desejada: \n'
              '1-Consultar Todos os Colaboradores \n'
              '2-ConsulTar Colaborador por id \n'
              '3-Consultar Colaborador(es) por Setor \n'
              '4-Retornar')
        op = input()
        # Entra com a opção e exibe a consulta desejada
        global lista_colaboradores
        if op == '1':
            print(20 * '-')
            # percorre a lista e mostra todos os colaboradores
            for item in lista_colaboradores:
                print('id : {}'.format(item['id']))
                print('nome : {}'.format(item['nome']))
                print('setor : {}'.format(item['setor']))
                print('pagamento : {}'.format(item['pagamento']))
                continue
        elif op == '2':
            op = int(input('Digite o id do colaborador:'))
            print(20 * '-')
            # busca pelo id e mostra o colaborador
            for item in lista_colaboradores:
                if op == item['id']:
                    print('id : {}'.format(item['id']))
                    print('nome : {}'.format(item['nome']))
                    print('setor : {}'.format(item['setor']))
                    print('pagamento : {}'.format(item['pagamento']))
                    continue
        elif op == '3':
            op = input('Digite o setor do(s) colaborador(es):')
            print(20 * '-')
            #  busca pelo id e mostra o(s) colaborador(es)
            for item in lista_colaboradores:
                if op == item['setor']:
                    print('id : {}'.format(item['id']))
                    print('nome : {}'.format(item['nome']))
                    print('setor : {}'.format(item['setor']))
                    print('pagamento : {}'.format(item['pagamento']))
                    continue
        elif op == '4':
            break


def remover_colaborador():
    global lista_colaboradores
    print(73 * '*')
    print(24 * '-' + ' MENU REMOVER COLABORADOR ' + 23 * '-')
    op = int(input('Digite o id do colaborador a ser removido:'))
    # busca pelo id e remove o colaborador
    for item in lista_colaboradores:
        if op == item['id']:
            lista_colaboradores.remove(item)


lista_colaboradores = []
id_global = 0
print('Bem-vindo(a) ao Controle de Colaboradores de Raphael Mendes Toso')
while True:
    print(73 * '*')
    print(29 * '-' + ' MENU PRINCIPAL ' + 28 * '-')
    print('Escolha a opção desejada: \n'
          '1-Cadastrar Colaborador \n'
          '2-ConsulTar Colaborador(es) \n'
          '3-Remover Colaborador \n'
          '4-Sair')
    op = input()
    # entra com a opção e chama a função apropriada, ou encerra o programa
    if op == '1':
        id_global += 1
        cadastrar_colaborador(id_global)
        continue
    elif op == '2':
        consultar_colaborador()
        continue
    elif op == '3':
        remover_colaborador()
        continue
    elif op == '4':
        break
