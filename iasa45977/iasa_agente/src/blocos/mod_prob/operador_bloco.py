"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

import copy
from src.blocos.mod_prob.estado_bloco import EstadoBloco
from src.lib.mod.operador import Operador

"""
Classe operadorBloco que é um tipo de operador, ou seja, implementa a interface Operador
e os seus métodos.

Esta implementação faz com que o nosso problema possa ser implementado, ou seja, irá representar
a transição de estados (estados esses que são movimentos de peças entre posições do "tabuleiro")
e o seu respectivo custo.
"""

class OperadorBloco(Operador):

    """
    Método construtor da classe OperadorBloco.

    São recebidos dois parâmetros correspondentes ao tipo de ação (empilhar ou desempilhar) e a posição
    para a qual/de qual será aplicado o movimento. Por exemplo, se for recebido "Desempilhar, 2", irá ser
    retirado o bloco da primeira posição da primeira pilha e irá movimentar o bloco para a primeira
    posição da terceira pilha, isto porque as 3 pilhas são numeradas pelos números 0, 1 e 2.

    São inicializadas variáveis a partir dos valores recebidos.

    @:param tipo_de_op
    @:param para_pos
    """

    def __init__(self, tipo_de_op, para_pos):
        self._tipo_de_op = tipo_de_op
        self._para_pos = para_pos

    """
    Método aplicar da classe OperadorBloco, implementado a partir do metódo abstrato da interface Operador.

    Irá ser aplicado o tipo de transição recebido no construtor, caso a pilha não esteja vazia, por exemplo,
    não será possível desempilhar da primeira pilha caso não existam blocos na mesma.

    Caso seja possível aplicar a transição, o bloco é sempreretirado da primera posição da pilha e posto na
    primeira posição da pilha de destino.

    @:param estado (pilhas antes da movimentação de blocos)
    @:return estado (pilhas depois da movimentação de blocos)
    """

    def aplicar(self, estado):
        pilhas = copy.deepcopy(estado)

        if self._tipo_de_op == "Desempilhar":
            if pilhas[0]:
                val = pilhas[0].pop(0)
                pilhas[self._para_pos].insert(0, val)
                return EstadoBloco(pilhas)

        else:
            if pilhas[self._para_pos]:
                val = pilhas[self._para_pos].pop(0)
                pilhas[0].insert(0, val)
                return EstadoBloco(pilhas)
            
    """
    Método custo da classe OperadorBloco, implementado a partir do metódo abstrato da interface Operador.

    Retorna o custo que a movimentação teve. O custo é igual ao número da pilha recebido, independentemente
    se a ação é desempilhar ou empilhar.

    @:param estado
    @:param estado_suc
    @:return custo
    """
        
    def custo(self, estado, estado_suc):
        return self._para_pos
    
    """
    Método que altera o output quando é invocado str() referente ao operador.
    """
        
    def __repr__(self):
        return f'{self._tipo_de_op}({self._para_pos})'
