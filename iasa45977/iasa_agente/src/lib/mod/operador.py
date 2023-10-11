"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Interface Operador

Esta interface faz parte do modelo de um problema, sendo o Operador o segundo ponto do mesmo.
Representa um transição entre estados. Um operador aplicado a um estado irá gerar um novo
estado. Irá definir também um custo de transição de estado.

Cada método desta interface irá ser implementado a posteriori pela classe que dela extende.
"""

class Operador(ABC):

    """
    Método abstrato aplicar da interface Operador.

    Como referido a cima, um operador aplicado a um estado irá gerar um novo estado. Assim,
    a classe aplicar recebe um estado ao qual vai aplicar a transição e irá retornar o estado
    que resulta da transição.

    @:param estado
    @:return estado
    """

    @abstractmethod
    def aplicar(self, estado):
        ""

    """
    Método abstrato custo da interface Operador.

    Este método irá devolver o custo (double) de transição entre os dois estados ("original" e "sucessor").

    @:param estado
    @:param estado_suc
    @:return custo
    """

    @abstractmethod
    def custo(self, estado, estado_suc):
        ""