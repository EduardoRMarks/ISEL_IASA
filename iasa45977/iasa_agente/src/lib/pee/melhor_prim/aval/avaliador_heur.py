"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.mec_proc.fronteira.avaliador import Avaliador

"""
Classe AvaliadorHeur que é um tipo de Avaliador. 

Este avaliador utiliza uma heurística que será implementada dependendo do tipo de
heuristica utilizada, onde o seu objectivo é guardar a mesma.
"""

class AvaliadorHeur(Avaliador):

    """
    Método definir_heuristica da classe AvaliadorHeur.

    Este método recebe e define uma heurística dependendo do tipo de heurística utilizada
    pelo avaliador.

    @:param heuristica
    """

    def definir_heuristica(self, heuristica):
        self._heuristica = heuristica