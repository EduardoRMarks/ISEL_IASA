"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

"""
Classe AvaliadorSof que herda da classe AvaliadorHeur.

Esta classe é um dos avaliadores baseados na heurística.

Este avaliador tem como objectivo a minimização da estimativa de custo para atingir
o objectivo, não tem em conta o custo do percurso explorado e as suas soluções são
sub-óptimas, podemos assim chegar à conclusão que f(n) = h(n).
"""

class AvaliadorSof(AvaliadorHeur):

    """
    Método prioridade da classe AvaliadorSof.

    Este método irá devolver a prioridade, ou seja, a estimativa do custo do nó recebido. Como
    f(n) = h(n), o método irá devolver apenas o resultado de h().

    @:param no
    @:return prioridade (estimativa do custo)
    """

    def prioridade(self, no):
        return self._heuristica.h(no.estado)