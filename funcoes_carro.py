from carro import Volks
from carro import Chevrolett
from carro import Hyundai
from carro import Fiat
import pickle


carros_cadastrados = []

def cadastrar_carro(carro, portas, ar_condicionado, direcao,
                 cor, ano, placa, load_car):
    if carro == 'Volks':
        carro = Volks(portas, ar_condicionado, direcao,
                 cor, ano, placa)
        load_car.append(carro)
    elif carro == 'Chevrolett':
        carro = Chevrolett(portas, ar_condicionado, direcao,
                      cor, ano, placa)
        load_car.append(carro)
    elif carro == 'Hyundai':
        carro = Hyundai(portas, ar_condicionado, direcao,
                           cor, ano, placa)
        load_car.append(carro)
    elif carro == 'Fiat':
        carro = Fiat(portas, ar_condicionado, direcao,
                           cor, ano, placa)
        load_car.append(carro)


def ver_carros(carros_cadastrados):
    for i in carros_cadastrados:
        print(i.modelo, i.valor_diaria)


def ver_detalhes_carro(load_car, posicao: int):
    ver_detalhes_do_carro = load_car[posicao]
    modelo = ver_detalhes_do_carro.modelo
    ar_condicionado = ver_detalhes_do_carro.ar_condicionado
    direcao = ver_detalhes_do_carro.direcao
    cor = ver_detalhes_do_carro.cor
    ano = ver_detalhes_do_carro.ano
    placa = ver_detalhes_do_carro.placa
    return 'Modelo: {}\nAr condicionado: {}\nDireção: {}\nCor: {}\n' \
           'Ano: {}\nPlaca: {}'.format(modelo, ar_condicionado, direcao,
                                       cor, ano, placa)


def save_car(load_car):
    try:
        with open('basecar.db', 'wb') as file:
           pickle.dump(load_car, file)
    except Exception as e:
        print('Erro ao salvar')
        print(e)


def load_car():
    try:
        with open('basecar.db', 'rb') as file:
            lista_carros = pickle.load(file)
            return lista_carros
    except Exception as e:
        print('Erro ao carregar')
        print(e)





