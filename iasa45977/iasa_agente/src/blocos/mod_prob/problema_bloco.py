"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.blocos.mod_prob.estado_bloco import EstadoBloco
from src.blocos.mod_prob.operador_bloco import OperadorBloco
from src.lib.mod.problema.problema import Problema

"""
Classe ProblemaBloco que extende de Problema.

Esta classe tem o objectivos de tratar do problema/cenário do caso prático tendo um estado
inicial ([2, 3, 1], [], []), um estado final ([1, 2, 3], [], []) e uma lista de movimentos
possíveis para o problema.
"""

class ProblemaBloco(Problema):

    """
    Método construtor da classe ProblemaBloco.

    É chamado o método construtor da super classe, que recebe um estado inicial e uma lista de operadores.
    Para tal, instanciamos a classe EstadoBloco passando o estado inicial como parâmetro. Repetimos o mesmo
    procedimento para os operadores instanciando cada operador recebido através da classe OperadorBloco.

    Por fim, inicializamos uma variável local para representar o estado final, instanciando, tal como atrás,
    a classe EstadoBloco com o parâmetro recebido estado_final.

    @:param movimentos
    @:param estado_inicial
    @:param estado_final
    """
    
    def __init__(self, movimentos, estado_inicial, estado_final):
        super().__init__(EstadoBloco(estado_inicial), [OperadorBloco(movimento.movimento,
                                                            movimento.posicao) for movimento in movimentos])
        
        self._pilhas_fin = EstadoBloco(estado_final)

    """
    Método objectivo da classe ProblemaBloco implementada a partir do método asbtrato da super classe.

    Retorna um booleano caso o estado recebido seja o estado final.

    @:param estado
    @:return true/false
    """

    def objectivo(self, estado):
        return self._pilhas_fin == estado