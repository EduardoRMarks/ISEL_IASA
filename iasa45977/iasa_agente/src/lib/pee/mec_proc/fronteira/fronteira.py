"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Classe abstrata Fronteira

A classe Fronteira, no raciocínio automático com base em PEE (Procura em espaços de estados),
permite inserir e remover nós de forma ordenada. Também indica se a fronteira está vazia.

Este mecanismo de procura explora os nós até chegar ao objectivo ou até já ter explorado a 
fronteira toda. 
"""

class Fronteira(ABC):

    """
    Atributo read only da classe Fronteira.
    Retorna true se a lista de nos estiver vazia e false caso não esteja vazia.
    """
    @property
    def vazia(self):
        if len(self._nos) == 0:
            return True
        else:
            return False
        
    @property
    def numero_nos(self):
        return len(self._nos)
    

    """
    Método construtor da classe Fronteira.

    Chama o método iniciar.
    """

    def __init__(self):
        self.iniciar()

    """
    Método iniciar

    Cria uma lista vazia de memoria.
    """

    def iniciar(self):
        self._nos = []

    """
    Método abstrato inserir da classe Fronteira.

    Este método insere um nó na fronteira, ou seja, na lista de nós. É um método abstrato pois
    o nó será inserido dependendo do tipo de fronteiras que estejam a ser usadas.

    @:param no
    """
    
    @abstractmethod
    def inserir(self, no):
        pass

    """
    Método remover da classe Fronteira.

    Este método remove o primeiro nó da fronteira.

    @:return lista de nos sem o no removido
    """
    
    def remover(self):
        return self._nos.pop(0)
