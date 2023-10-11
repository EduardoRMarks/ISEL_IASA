"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Classe Problema.

Esta classe faz parte do modelo de um problema, sendo o Problema o terceiro e último ponto do 
mesmo.

O raciocínio automático refere-se à capacidade de um sistema computacional resolver de forma 
automática um problema com base numa representação de conhecimento do respectivo domínio, produzindo 
uma solução a partir de diversas alternativas possíveis. Um problema tem um estado inicial (propriedade
read only da classe Estado), tem uma lista de operadores (outra propriedade read only da interface Operador) 
e uma função de teste de objectivo, ou seja, um objectico.

Como dito atrás, a classe Problema irá agregar a classe Estado e a interface Operador.
"""

class Problema(ABC):

    """
    Método construtor da classe Problema.

    Recebe no construtor um estado inicial e uma lista de operadores e guardam os mesmos em variáveis privadas

    @:param estado_inicial
    @:param operadores
    """
    
    def __init__(self, estado_inicial, operadores):
        self._estado_inicial = estado_inicial
        self._operadores = operadores

    """
    Método abstrato objectivo da classe Problema.

    Este método irá devolver um valor booleano que irá indicar se um estado recebido faz parte de um estado
    objectivo. Caso faça parte irá retornar true, caso contrario retorna false.

    @:param estado
    @:return true/false
    """
    
    @abstractmethod
    def objectivo(self, estado):
        ""

    """
    Propriedade read only do estado inicial
    """
    
    @property
    def estado_inicial(self):
        return self._estado_inicial
    
    """
    Propriedade read only dos operadores
    """
    
    @property
    def operadores(self):
        return self._operadores