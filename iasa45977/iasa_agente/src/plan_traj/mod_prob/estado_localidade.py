"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.mod.estado import Estado

"""
Classe EstadoLocalidade que é um tipo de Estado no contexto do problema, ou seja, uma
localidade no trajecto.

Como herda da classe estado, irá concretizar o método abstrato id_valor().
"""

class EstadoLocalidade(Estado):

    """
    Propriedade read-only da classe EstadoLocalidade. Retorna a localidade.
    """
    
    @property
    def localidade(self):
        return self._localidade
    
    """
    Método construtor da classe EstadoLocalidade.

    O construtor recebe uma localidade e inicializa-a.

    @:param localidade
    """
    
    def __init__(self, localidade):
        self._localidade = localidade

    """
    Método id_valor da classe EstadoLocalidade implementado a partir do método abstrato
    da classe Estado.

    Este método retorna o valor único (hash value), ou identificador, da localidade.

    @:return hash_value (identificador de estado)
    """

    def id_valor(self):
        return self._localidade.__hash__()
