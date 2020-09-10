

class Carro:
    """Classe genérica de carros."""

    def __init__(self, portas, ar_condicionado, direcao,
                 cor, ano, placa):
        self.portas = portas
        self.ar_condicionado = ar_condicionado
        self.direcao = direcao
        self.cor = cor
        self.ano = ano
        self.placa = placa


class Volks(Carro):
    """Classe que cria objeto carro volks."""

    marca = 'Volks'
    modelo = 'Polo'
    valor_diaria = 'R$ 100,00'

    def __str__(self):
        return '{}'.format(self.modelo)


class Chevrolett(Carro):
    """Classe que cria objeto carro chevrolett."""

    marca = 'Chevrolett'
    modelo = 'Cruize'
    valor_diaria = 'R$ 100,00'
    def __str__(self):
       return '{}'.format(self.modelo)


class Hyundai(Carro):
    """Classe que cria objeto carro hyundai."""

    marca = 'Hyundai'
    modelo = 'HB20'
    valor_diaria = 'R$ 100,00'
    def __str__(self):
        return '{}'.format(self.modelo)


class Fiat(Carro):
    """Classe que cria objeto carro fiat."""

    marca = 'Fiat'
    modelo = 'Linea'
    valor_diaria = 'R$ 100,00'
    def __str__(self):
        return '{}'.format(self.modelo)


class Ford(Carro):
    """Classe que cria objeto carro ford."""

    marca = ' Ford'
    modelo = 'Focus'
    valor_diaria = 'R$ 100,00'
    def __str__(self):
        return '{}'.format(self.modelo)









