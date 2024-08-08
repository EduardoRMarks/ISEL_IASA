"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""
from src.lib.pdm.mec_util import MecUtil

"""
Classe PDM (Processos de Decisão de Markov). Este processo de decisão tem como objectivo
a previsão e o controlo da sequência de iterações do agente segundo um ambiente.

Um problema que use este tipo de processo de decisão, define uma utilidade, que se trata do
efeito cumulativo da evolução da situação tendo em conta a história da evolução (sequência de
estados com ganhos e perdas) e uma recompensa, que é um ganho ou perda num determinado estado,
esse valor pode ser positivo ou negativo, mas sempre finito.

É também definida uma política comportamental. A política é uma forma de representação do
comportamento do agente e define qual a ação que o agente deve realizar em cada estado do mundo,
estratégia de ação.
"""

class PDM():

    """
    Método construtor da classe PDM.

    O constutor recebe os parâmetros modelo, gama e delta_max, parâmetros necessários para que
    este tipo de problema seja resolvido.

    Inicializa cada variável com uma variével local e incializa também o MecUtil, que irá ser necessário
    para se efetual os calculos da utilidade.

    @:param mdoelo
    @:param gama
    @:param delta_max
    """

    def __init__(self, modelo, gama, delta_max):
        self._modelo = modelo
        self._gama = gama
        self._delta_max = delta_max
        self._mec_util = MecUtil(self._modelo, self._gama, self._delta_max)
    
    """
    Método politica da classe PDM.

    Irá devolver a politica comportamental, ou seja, a estratégia de seleção de ação. Significa
    que a variável politica terá, para cada posição, o valor da ação com maior utilidade.

    @:param U
    @:return politica
    """

    def politica(self, U):
        S = self._modelo.S
        A = self._modelo.A
    
        politica = {s: max(A(s), key=lambda a: self._mec_util.util_accao(s, a, U)) 
                    for s in S() if A(s)}
        return politica

    
    """
    Método resolver da classe PDM.

    É calculada a utilidade, retornando a mesma e a politica em função da utilidade previamente calculada,
    ou seja, revolve o problema a parytir dos processos de decisão Markov.

    @:return utilidade
    @:return politica
    """

    def resolver(self):
        utilidade = self._mec_util.utilidade()
        return utilidade, self.politica(utilidade)