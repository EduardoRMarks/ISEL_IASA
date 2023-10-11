"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

"""
Classe No

Um Nó é um elemento constituinte da árvore de procura, mantendo informação do estado a que corresponde
o nó, o operador que gerou o estado a que corresponde o nó, o nó antecessor na árvore de procura, a 
profundidade do nó na árvore de procura e o custo do percurso correspondente ao nó. 

Esta classe irá também comparar o valor com outros nós.
"""

class No():

    """
    Atributos read only da classe no
    """
    @property
    def profundidade(self):
        return self._profundidade
    
    @property
    def custo(self):
        return self._custo
    
    @property
    def estado(self):
        return self._estado
    
    @property
    def operador(self):
        return self._operador
    
    @property
    def antecessor(self):
        return self._antecessor
    
    """
    Método construtor da classe No.

    A inicialização do construtor da classe No pode ser feita de duas formas distintas. Caso seja um
    nó raiz não tem atecessores, ou seja, o seu antecessor é None por omissão e todos os seus parâmetros, 
    menos o estado, terão o valor 0.

    Caso não seja um nó raiz o seu operador e antecessor serão instanciados com os parâmetros recebidos, o
    custo terá de ser calculado a partir do custo do antecessor mais o custo do antecessor até ao estado onde
    nos encontramos e a sua profundidade será incrimentada com uma unidade a mais do que a profundidade do antecessor.

    @:param estado
    @:param operador
    @:param antecessor
    """

    def __init__(self, estado, operador = None, antecessor = None):

        if antecessor:
            self._custo = antecessor.custo + operador.custo(antecessor.estado, estado)
            self._profundidade = antecessor.profundidade + 1
        else:
            self._profundidade = 0
            self._custo = 0

        self._estado = estado
        self._operador = operador
        self._antecessor = antecessor
        

    """
    Método __lt__() da classe No.

    Método lt, ou less-than, é um método especial que descreve o operador menor (<) em python.
    É um método útil para comparar o custo de dois nós.

    @:param no
    @:return true/false
    """

    def __lt__(self, no):
        return self._custo < no.custo