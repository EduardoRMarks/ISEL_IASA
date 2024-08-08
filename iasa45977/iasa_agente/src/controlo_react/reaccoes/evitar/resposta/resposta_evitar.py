"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

import random
from src.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from src.lib.sae.ambiente.direccao import Direccao

"""
Classe RespostaEvitar

É um tipo de resposta que extende da classe RespostaMover que, por sua vez, estende da classse Resposta.

Esta classe, ao contrário da classe RespostaMover, irá analisar se há obstaculos para evitar, caso haja
vê se existe alguma direção livre e se houver, move-se para essa direção. Caso não haja obstaculos continua 
com o movimento que tinha anteriormente.
"""


class RespostaEvitar(RespostaMover):
    """
    Método construtor da classe RespostaEvitar, que chama o construtor da classe pai (RespostaMover) com a
    direção inicial (ESTE, como é dito no enunciado). A classe RespostaMover irá chamar o contrutor da sua 
    classe pai (Resposta) que inicializara uma ação a partir da direção inicial da classe onde nos encontramos.

    Criamos também uma lista com as direções do enumerado Direccao.

    @:param dir_inicial
    """

    def __init__(self, dir_inicial=Direccao.ESTE):
        super().__init__(dir_inicial)
        self.__direccoes = list(Direccao)

    """
    Método activar() da classe c que irá chamar o método com o mesmo nome da classe Resposta.

    Começamos por verificar, a partir de uma percepção recebida, se existe contacto com um obstáculo. Caso não
    exista ativa-se a resposta na direção atual. Se houver contacto, verificamos se existe alguma das 4 direções
    livres, se não houver o método para de ser executado, se houver pelo menos uma direção livre, alteramos a
    direção do agente para a direção livre aleatória e ativamos a resposta com a nova direção.

    Para vermos se há alguma direção livre utilizamos o método privado __direccao_livre.

    @:param percepcao
    @:param intensidade
    """

    def activar(self, percepcao, intensidade):
        if percepcao.contacto_obst(self._accao.direccao):
            dir_l = self.__direccao_livre(percepcao)
            if dir_l is not None:
                self._accao.direccao = dir_l
                return super().activar(percepcao, intensidade)
        else:
            return super().activar(percepcao, intensidade)

    """
    Método privado __direccao_livre da classe RespostaEvitar que irá devolver uma direção livre.

    Neste método criamos uma lista que, caso haja direções livres, adicionamos a direção livre à lista. No fim 
    da verificação, irá ser escolhida uma das direções aleatóriamente e essa direção será retornada.

    @:param percepcao
    @:return direccao
    """

    def __direccao_livre(self, percepcao):
        listDirLivres = []

        for dir in self.__direccoes:
            if not percepcao.contacto_obst(dir):
                listDirLivres.append(dir)

        return random.choice(listDirLivres)
