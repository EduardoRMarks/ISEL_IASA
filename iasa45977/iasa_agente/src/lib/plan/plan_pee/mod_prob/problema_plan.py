"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from mod.problema.problema import Problema

"""
Classe ProblemaPlan que implementa a classe Problema.

É um tipo de problema do planeamento de trajecto com base no objectivo com menor custo.
"""

class ProblemaPlan(Problema):

    """
    Método construtor da classe ProblemaPlan.

    O construtor recebe o modelo de planeamento, ou seja, o modelo mundo e o estado final que
    corresponde ao objectivo com menos custo. É chamado o construtor da superclasse passando como
    argumentos o estado atual e os operadores do problema. É guardado ainda num variável privada o
    estado final, ou seja, objectivo.

    @:param modelo_plan
    @:estado_final
    """
    
    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final

    """
    Método objectivo da classe ProblemaPlan, implementado a partir do método abstrato da super classe.

    Retorna se determinado estado recebido corresponde ao estado final do problema.
    
    @:param estado
    @:return true/false
    """

    def objectivo(self, estado):
        return estado == self.__estado_final