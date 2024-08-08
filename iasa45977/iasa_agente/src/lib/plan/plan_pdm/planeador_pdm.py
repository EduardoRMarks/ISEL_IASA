"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.pdm.pdm import PDM
from src.lib.plan.modelo.modelo_pdm_plan import ModeloPDMPlan
from src.lib.plan.plan_pdm.plano_pdm import PlanoPDM
from src.lib.plan.planeador import Planeador

"""
Classe PlaneadorPDM que implementa a interface Planeador, ou seja, é um tipo de planeador.

Este planeador com base nos processos de decisão Markov irá planear a trajectória do nosso
agente tendo em conta o modelo do mundo e os objectivos (Alvos).
"""

class PlaneadorPDM(Planeador):

    """
    Método construtor da classe PlaneadorPDM.

    Recebe duas variáveis, gama (com valor por omissão 0.85) e delta_max (com valor por omissão 1).
    são inicializadas com variáveis com o nome das mesmas.
    
    Os valores de gama tem o objectivo de aplicar um desconto por passo aplicado à previsão do
    custo resultante do movimento, assim quando menor for a variável gama, mais provavelmente o
    agente não se irá mover, pois o valor da recompensa será muito baixo.

    @:param gama (por omissão = 0.85)
    @:param delta (por omissão = 1)
    """

    def __init__(self, gama = 0.5, delta_max = 1):
        self._gama = gama
        self._delta_max = delta_max
        
    """
    Método planear da classe PlaneadorPDM, implementado a partir da interface Planear.

    É instanciada a classe ModeloPDMPlan com os parâmetros modelo_plan e objectivos recebidas.
    A partir desta instanciação, instanciamos a classe PDM com o modelo instanciado e com as
    variáveis gama e delta recebidas no construtor.

    É calculada a utilidade e a política a partir do método resolver da classe PDM, e por fim
    retornamos um plano instanciando a classe PlanoPDM com a utilidade e politica calculada
    anteriormente.

    @:param modelo_plan
    @:param objectivos
    @:return PlanoPDM
    """

    def planear(self, modelo_plan, objectivos):
        pdm = PDM(ModeloPDMPlan(modelo_plan, objectivos), self._gama, self._delta_max)
        utilidade, politica = pdm.resolver()
        return PlanoPDM(utilidade, politica)