"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.melhor_prim.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.heur_euclidiana import HeurEuclidiana
from plan.plan_pee.mod_prob.heur_manhattan import HeurManhattan
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador

"""
Classe PlaneadorPEE que implementa a interface Planeador, ou seja, é um tipo de planeador.

Este planeador com base na procura em espaço de estados irá planear a trajectória do nosso
agente tendo em conta o modelo do mundo e os objectivos (Alvos). Utilizamos o tipo de 
procura A* que é completo e óptimo. A heuristica definida para o planeamento consiste na lista
de objectivos recebida e já organizada por menor custo, ou seja, menor distancia, onde iremos
assim escolher o primeiro nó para a heuristica pois é o que se encontra mais perto do agente.
"""

class PlaneadorPEE(Planeador):

    """
    Método construtor da classe PlaneadorPEE.

    É inicializado o tipo de procura que irá ser utilizado no planeamento do percurso, neste caso
    será a procura A*, como foi já referido.
    """

    def __init__(self):
        self._mec_pee = ProcuraAA()

    """
    Método planear da classe PlaneadorPEE, implementado a partir da interface Planear.

    Para a utilização do tipo de procura A*, tem de ser definido um tipo de heuristica. A heuristica, neste
    caso, será o objectivo com o menor custo, ou seja, o primeiro elemento da lista objectivos recebida.

    É inicializada e definida a heuristica e é feita a procura procura no espaço de estados tendo em conta a
    heuristica, devolvendo a solução, caso exista a mesma. É retornado, por último, o plano de ação tendo em
    conta a solução obtida na procura.

    @:param modelo_plan
    @:param objectivos
    @:return PlanoPEE
    """

    def planear(self, modelo_plan, objectivos):

        if self._h == 0:
            heur = "Distância de Manhattan"
            heuristica = HeurManhattan(objectivos[0])
        elif self._h == 1:
            heur = "Distância Euclidiana"
            heuristica = HeurEuclidiana(objectivos[0])
        else:
            heur = "Default"
            heuristica = HeurDist(objectivos[0])

        self._mec_pee._avaliador.definir_heuristica(heuristica)
        solucao = self._mec_pee.procurar(ProblemaPlan(modelo_plan, objectivos[0]), heuristica)

        print(heur + ":")
        print("Complexidade Temporal: " + str(self._mec_pee.get_nos_processados))
        print("Complexidade Espacial: " + str(self._mec_pee.get_max_mem))
        print()

        return PlanoPEE(solucao)
    

    """
    Método que define, na classe, um número que se irá traduzir no tipo de heuristica utilizada.

    @:param h
    """
    
    def definir_heuristica(self, h):
        self._h = h