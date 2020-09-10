from funcoes_carro import *
from funcoes import *



def load():
    try:
        with open('database.db', 'rb') as file:
            lista_cliente = pickle.load(file)
            return lista_cliente
    except Exception as e:
        print('Erro ao carregar')
        print(e)


def menu():
    print(
        '################################\n'
        '1 - Cadastrar Cliente\n'
        '2 - Ver Clientes Cadastrados\n'
        '3 - Cadastrar Carros\n'
        '4 - Ver Carros\n'
        '5 - Ver Histórico\n'
        '6 - Deletar Cliente\n'
        '0 - Desligar Sistema\n'
        '################################'
    )


if __name__=="__main__":
    while True:
        lista_cliente = load() # variavel tipo lista 'lista_cliente'
        lista_carro = load_car()
        menu() #mostra menu

        opcao = input('Digite uma opção: ')
        if opcao == '1':
            nome = input('Digite o nome:')
            cpf = input('Digite o cpf: ')
            rg = input('Digite o Rg: ')
            telefone = input('Insira o telefone: ')
            endereco = input('Insira o endereço')
            cad = cadastrar_cliente(nome, cpf, rg, telefone,
                                    endereco, lista_cliente)
            save(lista_cliente)
        elif opcao == '2':
            while True:
                for i in lista_cliente:
                    print(i)
                print(
                    '1 - ver dados do cliente\n'
                    '2 - Voltar ao menu principal'
                )
                escolha = input('Digite uma opção: ')
                if escolha == '1':
                    pos = input('Escolha um cliente: ')
                    dados_cliente = ver_cadastro_cliente(int(pos), lista_cliente)
                    print(dados_cliente)
                    break
                elif escolha == '2':
                    break
                else:
                    print('Digito inválido tente um digito valido 1 ou 2')
        elif opcao == '3':
            carro = input('Insira um modelo: ')
            portas = input('Insira a quantidade de portas: ')
            ar_condicionado = input('Insira se há ar condicionado: ')
            direcao = input('Insira o tipo de direção: ')
            cor = input('Insira a cor do veiculo: ')
            ano = input('Insira o ano: ')
            placa = input('Insira a placa: ')
            cadastrar_carro(carro, portas, ar_condicionado, direcao,
                            cor, ano, placa, lista_carro)
            save_car(lista_carro)
        elif opcao == '4':
            while True:
                ver_carros(lista_carro)
                print(
                    '1 - Ver detalhes do carro\n'
                    '2 - Alugar carro\n'
                    '3 - Voltar ao menu principal\n'
                )
                opcao = input('Escolha uma opção: ')
                if opcao == '1':
                    ver_detalhes = input('Escolha um carro'
                                         ' para ver os detalhes: ')
                    posicao = (int(ver_detalhes))
                    print(ver_detalhes_carro(lista_carro, posicao))

                elif opcao == '2':
                    posicao = input('cliente a alugar: ')
                    cliente = (int(posicao))
                    carro_a_ser_alugado = input('Digite o carro a ser alugado')
                    carro = (int(carro_a_ser_alugado))
                    carro_alugado = lista_carro[carro]
                    lista_cliente[cliente].alugar(carro_alugado)
                    rel = relatorio(lista_cliente[cliente], carro_alugado)
                    geradorRelatorio(lista_cliente[cliente], rel)
                    save(lista_cliente)
                    break
                elif opcao == '3':
                    break
                else:
                    print('Digito inválido tende um digito valido 1 ou 2')

        elif opcao == '5':
            while True:
                try:
                    ver_clientes_cadastrados(lista_cliente)
                    escolha = input('Escolha o Cliente: ')
                    cliente = lista_cliente[int(escolha)]
                    print(cliente.historico())
                    break
                except:
                    print('Cliente inexistente. Tente novamente')


        elif opcao == '6':
            escolha_cliente = input('Qual cliente deletar?: ')
            lista_cliente.pop(int(escolha_cliente))

        elif opcao == '0':
            print('Fechando Sistema...')
            break
        else:
            print('Digito invalido\n Tente novamente.')
