"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.pee.mec_proc.fronteira.fronteira import Fronteira

"""
Classe FronteiraFIFO

Classe FronteiraFIFO (Fronteira First In First Out) é uma forma de procura que funciona
como uma fila, onde o primeira a entrar vai ser o primero a sair, e o último a entrar será
o último a sair.  

Esta classe extende da classe Fronteira, pois a FronteiraFIFO é um tipo de fronteira, 
e irá implementar o método abstrato da mesma.
"""

class FronteiraFIFO(Fronteira):

    """
    Método inserir da classe FronteiraFIFO implementado a partir da classe mãe Fronteira.

    Como estamos perante o método de procura FIFO (First In First Out), o nó recebido será
    inserido na última posição da lista de nós.

    @:param no
    """

    def inserir(self, no):
        self._nos.append(no)

