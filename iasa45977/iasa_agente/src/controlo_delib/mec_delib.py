"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from sae.ambiente.elemento import Elemento

"""
Classe MecDelib (mecanimos deliberativo).

Esta classe tem como objectivo a deliberação de objectivos, ou seja, elementos do tipo alvo, retornando
uma lista organizada por distâncias mais pequenas entre o elemento do tipo alvo e o agente.
"""

class MecDelib():

    """
    Método construtor da classe MecDelib.

    O construtor recebe o modelo mundo e instacio o mesmo numa variável local.

    @:param modelo_mundo
    """

    def __init__(self, modelo_mundo):
        self._modelo_mundo = modelo_mundo

    """
    Método deliberar da classe MecDelib.

    É criado uma lista de objectivos, ou seja, de elementos "alvo" que é o objectivo para o qual o
    agente se irá mover. Caso a lista de objectivos não esteja vazia, organizamos de modo a que
    o primeiro elemento da lista seja o elemento mais próximo do agente e por fim retornamos a lista
    já organizada.

    @:return estados
    """

    def deliberar(self):
        estados = self._modelo_mundo.obter_estados()
        objectivos = [estado for estado in estados
                            if self._modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        
        if objectivos:
            objectivos.sort(key = lambda estado: self._modelo_mundo.distancia(estado))
            return objectivos