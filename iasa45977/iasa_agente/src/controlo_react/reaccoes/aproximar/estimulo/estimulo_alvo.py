"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""


"""
Classe EstimuloAlvo

Classe que implementara a interface Estimulo e que tem como objectivo detetar um alvo numa direção recebida.
"""


from src.lib.ecr.estimulo import Estimulo
from src.lib.sae.ambiente.elemento import Elemento


class EstimuloAlvo(Estimulo):
    """
    Construtor da classe EstimuloAlvo. Recebe uma direção, direção essa que será utilizada para fazer a deteção
    de um alvo. Irá inicializar duas variáveis privadas que serão utiliazadas no método detectar(). A variável
    gama fará com que quanto mais longe esteja o alvo, menos "importancia" tenha, ou seja, se um alvo estiver muito
    distante, o seu valor calculado na classe detetar há de se apróximar a 0, ocorre assim um decaimento da distância.
    Quanto mais baixo for o valor de gama mais depressa o valor chega a 0.

    Utilizamos este método de calculo pois a prioridade funciona com a procura do maior valor e sem o gama o maior valor
    seria do alvo mais distante.

    @:param direccao
    @:param gama
    """

    def __init__(self, direccao, gama=0.9):
        self.__direccao = direccao
        self.__gama = gama

    """
    Método da classe EstimuloAlvo concretizado a partir do método abstratato "detectar" da classe Estimulo.

    Este método irá detetar um elemento do mapa na direção recebida no construtor. Verificamos se o elemento recebido
    é um alvo do mapa, se for retorna a intensidade relativa à distância à qual se encontra do agente, caso constrário
    retornara uma intensidade de 0 (em float). decaimento

    @:param percepcao
    @:return intensidade
    """

    def detectar(self, percepcao):
        elm, dist, _ = percepcao[self.__direccao]

        return self.__gama**dist if elm is Elemento.ALVO else 0
