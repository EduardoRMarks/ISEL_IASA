"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

"""
Classe MecUtil.

Esta classe tem como objectivo o cálculo da utilidade de Estado. Para tal, irá ser utilizado
o algoritmo explicado a baixo. Irá calcular também o somatório da utilidade das ações. O algoritmo
irá parar de iterar quando a diferença máxima de atualização for menor que o delta máximo definido.
"""

class MecUtil():

    """
    Método construtor da classe MecUtil.

    O construtor recebe os parâmetros modelo, gama e delta máximo e cria variáveis locais com os
    mesmos nomes.

    @:param modelo
    @:param gama
    @:param delta_max
    """

    def __init__(self, modelo, gama, delta_max):
        self._modelo = modelo
        self._gama = gama
        self._delta_max = delta_max

    """
    Método utilidade da classe MecUtil.

    Irá calcular a utilidade de todos os estados segundo o algoritmo do cálculo da utilidade
    estudado em aula. 

    A sua implementação é a seguinte:
        1: É inicializada uma variável U (utilidade) sendo um dicionário de estados inicializado a zeros.
        2: É criada uma cópia do valor da utilidade anterior.
        3: O dicionário é iterado, obtendo o valor máximo da utiliadade da ação
            3.1: A utilidade da ação é calculada para todas as ações possíveis para a posição.
        4: É calculado o valor máximo de delta comparando o delta atual com o módulo da subtração entre o valor
        atual da utilidade com o valor aterior da mesma.
        5: São repetidos os passos 2, 3 e 4 até que o valor de delta seja maior que o valor máximo do mesmo
        recebido como parâmetro no construtor.
        6: Retorna-se o dicionário de utilidades.

    @:return U
    """

    def utilidade(self):
        S = self._modelo.S
        A = self._modelo.A

        U = {s:0 for s in S()}

        while True:
            u_aterior = U.copy()
            delta = 0

            for s in S():
                U[s] = max([self.util_accao(s, a, u_aterior) for a in A(s)], default = 0)
                delta = max(delta, abs(U[s] - u_aterior[s]))
            
            if delta < self._delta_max:
                break
        return U

    """
    Método util_accao da classe MecUtil.

    É a função que irá efectuar o ponto 3.1 anteriormente referido. Irá ser efectuado o somatório
    das utilidades de cada ação possível para a posição atual.

    @:param s (estado atual)
    @:param a (ação a ser aplicada)
    @:param U (utilidade anterior)
    @:return somatório das utilidades
    """

    def util_accao(self, s, a, U):
        T = self._modelo.T
        R = self._modelo.R
        A = self._modelo.A
        SL = []

        SL = [self._modelo._transicoes.get((s, accao))
              for accao in A(s) if self._modelo._transicoes.get((s, accao))]

        return sum(T(s, a, sl)*(R(s, a, sl) + self._gama * U[sl]) for sl in SL)