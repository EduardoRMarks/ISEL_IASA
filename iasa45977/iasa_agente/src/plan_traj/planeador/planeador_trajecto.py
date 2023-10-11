"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.larg.procura_largura import ProcurarLargura
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_profundidade import ProcuraProfundidade
from plan_traj.mod_prob.problema_plan_traj import ProblemaPlanTraj

"""
Classe PlaneadorTrajecto.

Esta classe tem como objectivo o planeamento de um trajecto. Para tal, teremos que escolher um dos
mecânismos de procura já implementados que irá posteriormente ou mostrar o caminho percorrido
para chegar ao destino ou, caso não exista uma solução, mostrar uma mensagem a informar que não
existe caminho possível.
"""

class PlaneadorTrajecto():

    """
    Método planear da classe PlaneadorTrajecto.

    Neste método, começamos por escolher o mecanismo de procura desejado para concretizar o planeamento
    do caminho desde a localidade inicial até à localidade final, localidede essas que são recebidas como
    parâmetros.

    Com o mecanismo, procuramos uma solução para o caminho desejado e caso exista caminho é escrito na
    consola que existe caminho e mostra na consola o mesmo.
    """

    def planear(self, ligacoes, loc_inicial, loc_final):

        """
        loc_inicial = 0
        loc_final = 4
        """

        #mecanismo_proc = ProcurarLargura()
        """
        Número de nós processados: 6
        Número máximo em memória: 3
        Loc-0  : None
        Loc-2  : Loc-0 -> Loc-2
        Loc-4  : Loc-2 -> Loc-4
        """

        mecanismo_proc = ProcuraCustoUnif()
        """
        Número de nós processados: 7
        Número máximo em memória: 3
        Loc-0  : None
        Loc-1  : Loc-0 -> Loc-1
        Loc-3  : Loc-1 -> Loc-3
        Loc-5  : Loc-3 -> Loc-5
        Loc-4  : Loc-5 -> Loc-4
        """

        #mecanismo_proc = ProcuraProfIter()
        """
        Número de nós processados: 3
        Número máximo em memória: 2
        Loc-0  : None
        Loc-2  : Loc-0 -> Loc-2
        Loc-4  : Loc-2 -> Loc-4
        """

        #mecanismo_proc = ProcuraProfLim()
        """
        Número de nós processados: 3
        Número máximo em memória: 2
        Loc-0  : None
        Loc-2  : Loc-0 -> Loc-2
        Loc-4  : Loc-2 -> Loc-4
        """

        #mecanismo_proc = ProcuraProfundidade()

        solucao = mecanismo_proc.procurar(ProblemaPlanTraj(ligacoes, loc_inicial, loc_final))

        #print("Número de nós processados: " + str(mecanismo_proc.get_nos_processados))
        #print("Número máximo em memória: " + str(mecanismo_proc.get_max_mem))

        return solucao, mecanismo_proc
