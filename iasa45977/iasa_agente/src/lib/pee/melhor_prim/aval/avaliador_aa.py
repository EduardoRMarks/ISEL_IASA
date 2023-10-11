"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

"""
Classe AvaliadorAA que herda da classe AvaliadorHeur.

Esta classe é um dos avaliadores baseados na heurística.

Este avaliador tem como objectivo a minimização do custo global, ou seja, o custo acumulado
até ao nó n mais o custo estimadoo até ao objectivo, podemos assim chegar à conclusão
que f(n) = g(n) + h(n).
"""

class AvaliadorAA(AvaliadorHeur):
    
    """
    Método prioridade da classe AvaliadorAA.

    Este método irá devolver a prioridade, ou seja, o custo acumulado até ao nó n mais a estimativa 
    do custo do nó recebido. Assim, o método irá devolver o custo do no recebido, mas o resultado de h().

    @:param no
    @:return prioridade (estimativa do custo)
    """

    def prioridade(self, no):
        return no.custo + self._heuristica.h(no.estado)