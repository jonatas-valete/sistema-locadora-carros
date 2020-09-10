from cliente import Cliente
import pickle

CLIENTES_CADASTRADOS = []

def save(loadfile):
    try:
        with open('database.db', 'wb') as file:
            pickle.dump(loadfile, file)
            print('Save')
    except Exception as e:
        print('Erro ao salvar')
        print(e)


def save_alugar(lista):
    try:
        with open('database.db', 'wb') as file:
            pickle.dump(lista, file)
            print('Save')
    except:
        print('erro ao salvar alugar')


def cadastrar_cliente(nome, cpf, rg, telefone, endereco, loadfile):
    cadastro = Cliente(nome, cpf, rg, telefone, endereco)
    loadfile.append(cadastro)
    print('Cadastrado com sucesso.')


def ver_clientes_cadastrados(lista):
     for cliente in lista:
         print(cliente)


def ver_cadastro_cliente(pos: int, lista):
    cliente = lista[pos]
    nome = cliente.nome
    cpf = cliente.cpf
    rg = cliente.rg
    telefone = cliente.telefone
    endereco = cliente.endereco
    return 'Nome: {}\nCpf: {}\nRg: {}' \
           '\nTelefone: {}\nEndereço: {}'.format(nome, cpf, rg,
                                              telefone, endereco)


def relatorio(cliente, carro_alugado):
    qnt_dias = input('Quantos dias alugar carro?: ')
    data = input('Qual a data do aluguel?: ')
    valor = input('Qual o valor total do aluguel?: ')
    return (
        '-----------------------------------------------------------\n'
        'Nome: {} - Carro alugado: {} - Carro alugado a {} dias - \n'
        'Valor: {} - Data do aluguel: {}\n'.format(cliente, carro_alugado,
                                                  qnt_dias, valor, data)

    )


def geradorRelatorio(nome_cliente, relatorio):
    nome_arquivo = '{}.txt'.format(nome_cliente)
    try:
        with open('{}'.format(nome_arquivo), 'a') as file:
            file.write('{}'.format(relatorio))
            file.close()
    except Exception as e:
        print('Erro ao gerar relatório')
        print(e)
