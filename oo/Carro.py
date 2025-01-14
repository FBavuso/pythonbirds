"""
Voçê deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direcao

O Motor terá a responsabilidade de controlar a velocidade.
ele oferece os seguintes atributos:
1) atributo de dado valocidade
2) metodo acelerar, que devera incrementar na velocidade uma unidade
3) metodo frear, que devera decrementar a velocidade em duas unidades

A Direcao tera a responsabilidade de controlar a direcao.
ela oferece os seguintes atributos:
1) valor de direçao com valores possiveis : Norte, Sul, Leste , Oeste
2) metodo girar_a_direita
3) metodo girar_a_esquerda

   N
O     L
   S

   Exemplo:
   >>> # Testando Motor
   >>> motor = Motor()
   >>> motor.velocidade
   0
   >>> motor.acelerar()
   >>> motor.velocidade
   1
   >>> motor.acelerar()
   >>> motor.velocidade
   2
   >>> motor.acelerar()
   >>> motor.velocidade
   3
   >>> motor.frear()
   >>> motor.velocidade
   1
   >>> motor.frear()
   >>> motor.velocidade
   0
   >>> #Testando Direcao
   >>> direcao = Direcao()
   >>> direcao.valor
   'Norte'
   >>> direcao.girar_a_direita()
   >>> direcao.valor
   'Leste'
   >>> direcao.girar_a_direita()
   >>> direcao.valor
   'Sul'
   >>> direcao.girar_a_direita()
   >>> direcao.valor
   'Oeste'
   >>> direcao.girar_a_direita()
   >>> direcao.valor
   'Norte'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Oeste'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Sul'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Leste'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Norte'

   >>> carro = Carro(direcao, motor)
   >>> carro.calcular_velocidade()
   0
   >>> carro.acelerar()
   >>> carro.calcular_velocidade()
   1
   >>> carro.acelerar()
   >>> carro.calcular_velocidade()
   2
   >>> carro.frear()
   >>> carro.calcular_velocidade()
   0
   >>> carro.calcular_direcao()
   'Norte'
   >>> carro.girar_a_direita()
   >>> carro.calcular_direcao()
   'Leste'
   >>> carro.girar_a_esquerda()
   >>> carro.calcular_direcao()
   'Norte'
   >>> carro.girar_a_esquerda()
   >>> carro.calcular_direcao()
   'Oeste'



"""

class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade == 1:
            self.velocidade -= 1
        else:
            self.velocidade -= 2
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    rodar_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rodar_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rodar_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rodar_a_esquerda_dct[self.valor]

class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()