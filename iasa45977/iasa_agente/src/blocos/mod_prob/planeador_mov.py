"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from blocos.mod_prob.estado_bloco import EstadoBloco
from blocos.mod_prob.heur_bloco import HeurBloco
from blocos.mod_prob.problema_bloco import ProblemaBloco
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from plan.planeador import Planeador

"""
Classe PlaneadorMov que implementa a Interface Planeador.

Esta classe, como o nome indica, tem como objectivo o planeamento do "trajecto", ou seja, o planeamento
dos movimentos dos blocos.

Para tal, teremos que escolher um dos mecânismos de procura já implementados que irá posteriormente ou 
mostrar o caminho percorrido para chegar ao destino ou, caso não exista uma solução, mostrar uma mensagem 
a informar que não existe caminho possível.
"""

class NPlaneadorMov(Planeador):

    """
    Método planear da classe PlanearMov implementada a partir da classe abstrata planear da interfce Planeador.

    Para ser efectuado o planeamento, começamos por instanciar um problema a partir do 3 parâmetros recebidos.
    É depois definido um mecanismo de procura e, dependendo do mesmo, iremos ter que instanciar uma heuristica
    e definir a mesma no mecanismo de procura. Por último, irá ser procurada uma solução a partir do problema
    instanciado e, caso seja necessário para o tipo de procura, a heuristica definida.

    Retorna a solução e o mecanismo de procura que irá ser utilizado para a amostragem dos resultados.

    @:param movimentos
    @:b_init
    @:b_fin
    @:return solucao
    @:return mecanismo_proc
    """

    def planear(self, movimentos, b_init, b_fin):

        problema = ProblemaBloco(movimentos, b_init, b_fin)
        mecanismo_proc = ProcuraAA()
        heuristica = HeurBloco(b_fin)
        mecanismo_proc._avaliador.definir_heuristica(heuristica)
        solucao = mecanismo_proc.procurar(problema, heuristica)

        """problema = ProblemaBloco(movimentos, b_init, b_fin)
        mecanismo_proc = ProcuraCustoUnif()
        solucao = mecanismo_proc.procurar(problema)"""
        
        return solucao, mecanismo_proc