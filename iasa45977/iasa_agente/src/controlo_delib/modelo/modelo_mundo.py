"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from math import dist
from controlo_delib.modelo.operador_mover import OperadorMover
from mod.agente.estado_agente import EstadoAgente
from plan.modelo.modelo_plan import ModeloPlan
from sae.ambiente.direccao import Direccao

"""
Classe ModeloMundo que representa o mundo, ou seja, o mapa, por onde o agente irá navegar,
mundo esse que irá sendo atualizado ao longo do tempo.
"""

class ModeloMundo(ModeloPlan):

    """
    Propriedade read only que irá informar se houve uma modificação no mundo a navegar.
    """
    @property
    def alterado(self):
        return self._alterado

    """
    Método construtor da classe ModeloMundo.

    O construtor inicializa 5 variáveis sendo elas a variável bool "alterado" que se inicializa a false
    e que irá ser posta a true quando houver uma modificação no mundo a navegar, uma variável "estado"
    inicializada a None que irá representar o estado do agente em determinada altura da navegação bem como
    uma lista de estados, do tipo EstadoAgente. É inicializado a variável "elementos" que, para cada posição,
    irá representar se o elemento é um agente, um alvo, um obstáculo ou um vazio. Por fim, é inicializado uma
    lista de operadores a partir do domínio do problema.
    """

    def __init__(self):
        self._alterado = False
        self._estados = []
        self._elementos = {}
        self._operadores = [OperadorMover(self, direcao) for direcao in Direccao]

    """
    Método obter_estado. Retorna o estado atual do modelo.

    @:return estado
    """ 

    def obter_estado(self):
        return self._estado
    
    """
    Método obter_estados. Retorna a lista de estados do modelo.

    @:return estados
    """
    
    def obter_estados(self):
        return self._estados
    
    """
    Método obter_operadores. Retorna a lista de operadores do modelo.

    @:return operadores
    """

    def obter_operadores(self):
        return self._operadores
    
    """
    Método obter_elemento. Retorna um elemento da lista de elementos referente à posição
    do estado recebido.

    @:param estado
    @:return elemento
    """

    def obter_elemento(self, estado):
        return self._elementos.get(estado.posicao)
    
    """
    Método distancia da classe ModeloMundo.

    Este método tem como objectivo calcular a distância entre o estado atual e o estado recebido
    como parâmetro, Retornado o valor da distancia entre ambos.

    @:param estado
    @:return distancia
    """

    def distancia(self, estado):
        return dist(estado.posicao, self._estado.posicao)

    """
    Método actualizar da classe ModeloMundo.

    Este método irá aplicar o processo de atualização do mundo.

    O primeiro passo será atualizar o estado atual, ou seja, o estado do agente com base na sua posição.
    A seguir, iremos verificar se os elementos percepcionados não se alteraram. Caso não se tenham alterado,
    atualizamos a variável "alterado" com o valor False, Caso contrário, começamos por atualizar os elementos e 
    atualizamos também os estados, sendo que a atualização tem que ser feita através de objectos EstadoAgente 
    para cada posição. Por fim, atualizamos a variável "alterado" anteriormente mencionada para True.

    @:param percepcao
    """

    def actualizar(self, percepcao):
        self._estado = EstadoAgente(percepcao.posicao)

        if percepcao.elementos == self._elementos:
            self._alterado = False
        else:
            self._elementos = percepcao.elementos
            self._estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
            self._alterado = True

    """
    Método mostrar da classe ModeloMundo.

    Este método permite que a visualização do agente, alvos e obstáculos seja possível.

    @:param vista
    """

    def mostrar(self, vista):
        vista.mostrar_elementos(self._elementos)
        vista.marcar_posicao(self._estado.posicao)