"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.pdm.modelo.modelo_pdm import ModeloPDM
from src.lib.plan.modelo.modelo_plan import ModeloPlan

"""
Classe ModeloPDMPlan que implementa as interfaces ModeloPlan e ModeloPDM, logo, implementa
todos os seus métodos. É uma classe de modulação para ser utilizada na resolução de um problema
que utiliza o processo de Markov.

Ao utilizar a interface ModeloPlan garantimos que o código implementado anteriormente é compatível
com o problema proposto.
"""

class ModeloPDMPlan(ModeloPlan, ModeloPDM):

    """
    Método construto da classe ModeloPDMPlan.

    Recebe como atributos o modelo planeador, uma lista de objectivos e inicializa variáveis com
    estes atributos. Tem também uma variável rmax (recompensa máxima) inicializada com o valor
    1000 caso não seja passado nenhum parâmetro.

    É inicializado também um array de trasições possíveis no contexto do processo de decisão. Só é
    adicionada uma transição caso o estado quando é feito o aplicar exista.

    @:param modelo_plan
    @:param objectivos
    @:param rmax (=1000)
    """
     
    def __init__(self, modelo_plan, objectivos, rmax = 1000):
        self._modelo_plan = modelo_plan
        self._objectivos = objectivos
        self._rmax = rmax
        self._transicoes = {}

        for s in self.obter_estados():
            for a in self.obter_operadores():
                if sl:= a.aplicar(s):
                    self._transicoes[(s,a)] = sl
    
    """
    Método obter_estado implementado a partir da interface ModeloPlan.

    Retorna o estado atual no modelo mundo.

    @:return estado
    """

    def obter_estado(self):
        return self._modelo_plan.obter_estado()
    
    """
    Método obter_estados implementado a partir da interface ModeloPlan.
    
    Retorna a lista de estados no domínio do modelo mundo.

    @:return estados
    """
    
    def obter_estados(self):
        return self._modelo_plan.obter_estados()
    
    """
    Método obter_operadores implementado a partir da interface ModeloPlan.
    
    Retorna a lista de operadores no domínio do modelo mundo.

    @:return operadores
    """
    
    def obter_operadores(self):
        return self._modelo_plan.obter_operadores()
    
    """
    Método S implementado a partir da interface ModeloPDM.

    Na representação do problema sobre a for de PDM, S diz respeito ao conjunto
    de estados do mundo, e é isso que o método retorna.

    @:return estados
    """
    
    def S(self):
        return self.obter_estados()
    
    """
    Método A implementado a partir da interface ModeloPDM.

    Na representação do problema sobre a for de PDM, A diz respeito ao conjunto
    de ações possíveis no estado s se pertence a S, logo s não pode pertencer aos
    objectivos para ter uma operação possível.

    @:param s (estado)
    @:return lista de operadores
    """
    
    def A(self, s):
        return self.obter_operadores()
        
    """
    Método T implementado a partir da interface ModeloPDM.

    Na representação do problema sobre a for de PDM, T diz respeito à probabilidade
    de transição do estado s para o estado sn através de a. Irá retornar a probabilidade
    1 se a transição necessária existir no array de transições, caso contrário a
    probabilidade é 0.

    @:s (estado atual)
    @:a (operador)
    @:sn (estado seguinte)
    @:return 0/1 (probabilidade)
    """
        
    def T(self, s, a, sl):
        return 1 if sl == self._transicoes.get((s, a)) else 0

        
    """
    Método R implementado a partir da interface ModeloPDM.

    Na representação do problema sobre a for de PDM, R diz respeito à recompensa
    esperada na transição do estado s para o estado sn através do operador a. A
    recompensa é calculada a partir do custo do operador (é negativo pois está a mover-se,
    ou seja, perde energia). Caso o estado seguinte pertença à lista de objectivos soma-se
    a recompensa máxima.
    
    @:s (estado atual)
    @:a (operador)
    @:sn (estado seguinte)
    @:recompensa
    """

    def R(self, s, a, sl):
        if sl in self._objectivos:
            return -a.custo(s, sl) + self._rmax
        else:
            return -a.custo(s, sl)
