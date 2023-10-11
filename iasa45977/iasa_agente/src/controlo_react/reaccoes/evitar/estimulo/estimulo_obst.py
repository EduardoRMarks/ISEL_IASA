"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""


from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento

"""
Classe EstimuloObst

Classe que implementara a interface Estimulo e que tem como objectivo detetar um obstaculo numa direção recebida.
"""


class EstimuloObst(Estimulo):
    """
    Construtor da classe EstimuloObst. Recebe uma direção, direção essa que será utilizada para fazer a deteção
    de um obstaculo. Irá inicializar duas variáveis privadas que serão utiliazadas no método detectar(). A variável
    intensidade irá servir para ser retornada caso haja contacto com um obstaculo.

    @:param direccao
    @:param intensidade
    """

    def __init__(self, direccao, intensidade=1.0):
        self.__direccao = direccao
        self.__intensidae = intensidade

    """
    Método da classe EstimuloObst concretizado a partir do método abstratato "detectar" da classe Estimulo.

    Este método irá detetar um elemento do mapa na direção recebida no construtor. Verificamos se o elemento recebido
    é um obstáculo do mapa, se for retorna a intensidade igual a 1, caso constrário retornara uma intensidade de 0 (em float).

    @:param percepcao
    @:return intensidade
    """

    def detectar(self, percepcao):
        elm, dist, _ = percepcao[self.__direccao]

        return self.__intensidae if elm is Elemento.OBSTACULO else 0
