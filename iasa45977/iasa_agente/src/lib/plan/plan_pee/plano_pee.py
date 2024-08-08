"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.plan.plano import Plano

"""
Classe PlanoPEE que implementa a interface Plano, ou seja, é um tipo de plano baseado na
Procura em Espaço de Estados.

Tendo conhecimento do estado atual e do objectivo, irá ser planeado um conjunto de acções
a serem realizadas pelo agente de maneira que o mesmo chegue ao objectivo.
"""

class PlanoPEE(Plano):

    """
    Método construtor da classe PlanoPEE.

    Como na procura em espeço de estados o objectivo é conhecido pelo planeador, então é passado para
    o construtor do PlanoPEE a solução (objectivo).

    @:param solucao
    """

    def __init__(self, solucao):
        self._solucao = solucao

    """
    Método obter_accao da classe PlanoPEE implementado a partir da interface Plano.

    Irá devolver um operador a aplicar a partir do estado recebido, isto caso não haja
    modificações no mundo, o que fará com que o plano seja inválido. O método então irá
    percorrer toda a solução recebida no construtor, devolvendo o operador de cada nó
    enquanto a solução for maior que 1, ou seja, não esteja vazia.

    @:param estado
    @:retutn operador
    """

    def obter_accao(self, estado):
        if self._solucao.dimensao > 1:
            if estado == self._solucao[0].estado:
                self._solucao.remover()
                return self._solucao[0].operador

    """
    Método mostrar da classe PlanoPEE, implementado a partir da interface Plano.

    Este método mostra a solução (caminho desde a posição do agente até à podição do Alvo)
    a partir de uma vista recebida.

    @:param vista
    """

    def mostrar(self, vista):
        vista.mostrar_solucao(self._solucao)