"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""
from src.lib.mod.estado import Estado

"""
Classe EstadoBloco que é um tipo de Estado no contexto do problema, ou seja, o estado dos blocos em
cada uma das pilhas.

Como herda da classe estado, irá concretizar o método abstrato id_valor().
"""


class EstadoBloco(Estado):
    """
    Propriedade read-only da classe EstadoBloco.
    Retorna a posição dos blocos nas pilhas, ex [[1], [3, 2], []].
    """

    @property
    def blocos(self):
        return self._blocos

    """
    Método construtor da classe EstadoBloco.

    Recebe a posição dos blocos em cada pilha e inicializa uma variável local
    com a informação.

    @:param blocos
    """

    def __init__(self, blocos):
        self._blocos = blocos

    """
    Método id_valor da classe EstadoLocalidade implementado a partir do método abstrato
    da classe Estado.

    Este método retorna o valor único (hash value), ou identificador, dos blocos da pilha. Como não possível
    aplicar valores hash a listas, pois listas podem ser modificadas, agrupamos todos os elementos da lista
    das pilhas em tuplos, assim, torna-se possível a aplicação do identificador.

    @:return hash_value (identificador de estado)
    """

    def id_valor(self):
        self._blocos_tup = []
        for bloco in self._blocos:
            self._blocos_tup.append(tuple(bloco))

        return hash(tuple(self._blocos_tup))

    """
    Método que irá retornar o valor da pilha correspodente ao index recebido.
    
    @:param index
    @:return pilha
    """

    def __getitem__(self, index):
        return self._blocos[index]

    """
    Método que altera o output quando é invocado str() referente ao estado.
    """

    def __repr__(self):
        return f'{self.blocos}'
