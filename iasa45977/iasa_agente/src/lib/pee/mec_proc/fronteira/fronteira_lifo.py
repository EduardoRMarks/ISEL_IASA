"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.mec_proc.fronteira.fronteira import Fronteira

"""
Classe FronteiraLIFO

Classe FronteiraLIFO (Fronteira Last In First Out) é uma forma de procura onde último
nó a ser adicionado à árvore é o primeiro a ser explorado. 

Esta classe extende da classe Fronteira, pois a FronteiraLIFO é um tipo de fronteira, 
e irá implementar o método abstrato da mesma.
"""

class FronteiraLIFO(Fronteira):

    """
    Método inserir da classe FronteiraLIFO implementado a partir da classe mãe Fronteira.

    Como estamos perante o método de procura LIFO (Last In First Out), o nó recebido será
    inserido na primeira posição da lista de nós.

    @:param no
    """

    def inserir(self, no):
        self._nos.insert(0, no)

