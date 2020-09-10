

class Cliente:
    """classe que cria objeto cliente."""

    def __init__(self, nome, cpf, rg, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.endereco = endereco
        self.lista_carro = []

    def alugar(self, carro):
        self.lista_carro.append(carro)
        print('Carro alugado com sucesso')

    def historico(self):
            for carro in self.lista_carro:
                dados_carro = {
                    'marca': carro.marca, 'modelo': carro.modelo, 'portas': carro.portas,
                    'ar_condicionado': carro.ar_condicionado, 'direcao': carro.direcao,
                    'cor': carro.cor, 'ano': carro.ano, 'placa': carro.placa,
                }
                print(
                    dados_carro['marca'], dados_carro['modelo'],
                    dados_carro['portas'], dados_carro['ar_condicionado'],
                    dados_carro['direcao'], dados_carro['cor'],
                    dados_carro['ano'], dados_carro['placa']
                )

    def __str__(self):
        return '{}'.format(self.nome)



