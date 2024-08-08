"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.plan.plano import Plano

"""
Classe PlanoPDM que implementa a interface Plano, ou seja, é um tipo de plano baseado nos
Processos de Decisão de Markov.

Irá ser efectuado um planeamento de movimento tendo em conta a utilidade e politica, sendo
o caminho do agente até ao alvo o caminho com maior recompensa.
"""

class PlanoPDM(Plano):

    """
    Método construtor da classe PlanoPDM.

    Recebe com parâmetros a utilidade (efeito cumulativo da evolução da situação)
    e a política comportamental (define qual a ação que deve ser realizada em cada
    estado, ou seja, é a estratégia de ação). Inicializa variáveis com os mesmos nomes
    dos parâmetros recebidos.

    @:param utilidade
    @:param politica
    """

    def __init__(self, utilidade, politica):
        self._utilidade = utilidade
        self._politica = politica
        
    """
    Método obter_accao da classe PlanoPDM implementado a partir da interface Plano.

    Irá devolver um operador a aplicar a partir do estado recebido, sendo este obtido
    a partir da indexação da politica.

    @:param estado
    @:return operador
    """

    def obter_accao(self, estado):
        if self._politica:
            return self._politica[estado]
    
    """
    Método mostrar da classe PlanoPDM, implementado a partir da interface Plano.

    Este método irá mostrar a utilidade num gradiente de verde, quanto maior a utilidade, mais
    verde está o estado e irá demonstrar também a politica com setes amarelas. Estas duas
    demonstrações irão ser feitas para todos o modelo mundo, ao contrário da classe PlanoPEE
    que só era mostrado desde o agente até ao alvo mais próxiamo.

    Só é feita a mostração, caso hava politica e utilidade.

    @:param vista
    """
        
    def mostrar(self, vista):
        if self._politica:
            vista.mostrar_valor(self._utilidade)
            vista.mostrar_politica(self._politica)