"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Inteface Planeador.

Esta interface tem um método abstracto de seu nome planear que irá ser implementado
na classe que implementar esta interface.
"""

class Planeador(ABC):

    """
    Método abstracto planear. Na implementação, o método irá receber o modelo do mundo e uma
    lista de objectivos já organizada.
    """
    
    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        pass