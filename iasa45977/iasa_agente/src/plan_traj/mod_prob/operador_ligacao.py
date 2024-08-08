"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.mod.operador import Operador
from src.plan_traj.mod_prob.estado_localidade import EstadoLocalidade

"""
Classe OperadorLigacao que é um tipo de Operador, ou seja, implementa a interface Operador.

Esta implementação faz com que o nosso problema possa ser implementado, ou seja, irá representar
a transição de estados (estados esses que são localidades) e o seu respectivo custo.
"""

class OperadorLigacao(Operador):

    """
    Método construtor da classe OperadorLigacao.

    O construtor recebe 3 parâmetros, sendo esses a origem, o destino e o custo, e inicializa-os, sendo
    que tanto a origem como o destino são estados.

    @:param origem
    @:param destino
    @:param custo
    """

    def __init__(self, origem, destino, custo):
        self._custo = custo
        self._estado_origem = EstadoLocalidade(origem)
        self._estado_destino = EstadoLocalidade(destino)

    """
    Método aplicar da classe OperadorLigacao, implementado a partir do metódo abstrato da interface Operador.

    Este método irá aplicar o operador sobre o estado caso o estado recebido corresponde ao estado origem,
    caso contrário não retorna nada.

    @:param estado
    @:return estado (destino)
    """

    def aplicar(self, estado):
        if estado == self._estado_origem:
            return self._estado_destino
    
    """
    Método custo da classe OperadorLigacao, implementado a partir do metódo abstrato da interface Operador.

    No caso do nosso problema, não iremos usar os dois parâmetros estado e estado_suc, apenas vamos querer
    devolver o custo da aplicação do operador.

    @:param estado
    @:param estado_suc
    @:return custo
    """

    def custo(self, estado, estado_suc):
        return self._custo
    

    def __repr__(self):
        return f'{self._estado_origem.localidade} -> {self._estado_destino.localidade}'