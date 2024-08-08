"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from src.lib.ecr.prioridade import Prioridade
from src.lib.sae.ambiente.direccao import Direccao

"""
Classe AproximarAlvo

É uma classe que irá permitir uma aproximação ao alvo por parte do agente.

Chamamos a classe AproximarDir, que estende de Reaccao, para cada direção no nosso enumerado Direccao. Temos assim 
um comportamento composto onde a sua prioridade irá depender da distância entre o agente e o alvo mais próximo, ou seja,
se o agente estiver na presença de 4 alvos, irá dirigir-se para o mais próximo.
"""


class AproximarAlvo(Prioridade):
    """
    Método construtor da classe AproximarAlvo, que irá criar uma lista com instancias da classe AproximarDir, ou seja,
    uma lista com 4 direções distintas. Com a lista criada, irá ser chamado o super() da classe à qual herda.
    """

    def __init__(self):
        listDir = []

        for dir in Direccao:
            listDir.append(AproximarDir(dir))

        super().__init__(listDir)
