"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

"""
Classe ProcuraInformada, é um tipo de Procura Melhor-Primeiro.

Este tipo de procura são estratégias de exploração do espaço de estados que tiram partido de conhecimento 
do problema para ordenar a fronteira de exploração.

Para este tipo de procura, iremos usar uma heurística para obtermos uma estimativa do custo do percurso, ou
seja, irá "dizer" a ordem para a organização da fronteira.

Esta classe irá ser extendida por dois tipos de procura distintos, a ProcuraAA e a ProcuraSofrega.
"""

class ProcuraInformada(ProcuraMelhorPrim):

    """
    Método procurar da classe ProcuraInformada.

    Este método procura uma solução para o problema recebido usando o método do mesmo nome da super classe, tendo
    como diferença a heuristica caracteristica deste tipo de procura.

    @:param problema
    @:param heuristica
    @:return solucao
    """
    
    def procurar(self, problema, heuristica):
        self._heuristica = heuristica
        return super().procurar(problema)