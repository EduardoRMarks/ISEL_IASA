"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.deposito.mod_prob.problema_plan_dep import ProblemaPlanDep
from src.lib.pee.larg.procura_largura import ProcurarLargura
from src.lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from src.lib.pee.prof.procura_prof_iter import ProcuraProfIter
from src.lib.pee.prof.procura_prof_lim import ProcuraProfLim
from src.lib.pee.prof.procura_profundidade import ProcuraProfundidade


class PlaneadorDeposito():



    def planear(self, ligacoes, loc_inicial, loc_final):

        mecanismo_proc = ProcuraCustoUnif()
        

        solucao = mecanismo_proc.procurar(ProblemaPlanDep(ligacoes, loc_inicial, loc_final))

        #print("Número de nós processados: " + str(mecanismo_proc.get_nos_processados))
        #print("Número máximo em memória: " + str(mecanismo_proc.get_max_mem))

        return solucao, mecanismo_proc
