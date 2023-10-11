"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Classe abstrata Estado

Esta classe faz parte do modelo de um problema, sendo o Estado o primeiro ponto do mesmo.
Refere à identificação única por valor, em função da informação de estado.
"""

class Estado(ABC):

    """
    Método abstrato id_valor da classe Estado.

    Este método irá ser implementado no método que estender a classe Estado. A implementação
    irá devoler um valor inteiro único que irá identificar o valor do estado.
    """

    @abstractmethod
    def id_valor(self):
        ""

    """
    Método __hash__() da classe Estado.

    O método __hash__() recebe um objecto e retorna o valor do hash, ou seja, o valor representativo,
    como um número inteiro. Assim, ficamos com um valor de identificação para cada um dos estados.

    @:return hash_value  (identificador do estado)
    """
    
    def __hash__(self):
        return self.id_valor()
    
    """
    Método __eq__() da classe Estado.

    O método __eq__(), ou equals, irá comparar-se com o outro objecto recebido e irá retornar true caso
    os objectos sejam iguais. Dois objectos são iguais caso tenham a mesma identidade.

    @:param other (objecto para ser efetuada a comparação)
    @:return true/false
    """

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
