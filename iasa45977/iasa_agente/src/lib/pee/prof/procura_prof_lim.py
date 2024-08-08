"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.pee.prof.procura_profundidade import ProcuraProfundidade

"""
Classe ProcuraProfLim que extende da classe ProcuraProfundidade.

Este tipo de procura não é óptimo nem completo.

Esta classe é um tipo de procura em profundidade onde irá limitar a procura em profundidade 
até um certo valor de nós, fazendo assim com que o programa não procure infinitivamente 
passando por nós já explorados, os chamados ciclos.
"""

class ProcuraProfLim(ProcuraProfundidade):

    """
    Métodos getter e setter da variável privada prof_max.
    """
    @property
    def prof_max(self):
        return self._prof_max

    @prof_max.setter
    def prof_max(self, valor):
        self._prof_max = valor

    """
    Método construtor da classe ProcuraProfLim.

    Este método irá inicializar uma variável privada com o valor da profundidade máxima.
    
    @:param prof_max (com valor por omissão de 100)
    """

    def __init__(self, prof_max = 100):
        super().__init__()
        self._prof_max = prof_max

    """
    Método expandir da classe ProcuraProfLim.

    Irá expandir o nó caso a profundidade do mesmo seja mais pequena do que a
    profundidade máxima.

    @:param problema
    @:param no
    @:return lista de nós
    """

    def _expandir(self, problema, no):
        if (no.profundidade < self._prof_max):
            yield from super()._expandir(problema, no)


    """
    Método memorizar da classe ProcuraProfLim.

    O nó irá ser inserido na fronteira caso não esteja dentro de um ciclo.

    @:param no
    """

    def _memorizar(self, no):
        if not self._ciclo(no):
            super()._memorizar(no)

    """
    Método ciclo da classe ProcuraProfLim.

    Procura nos nós antecessores se o nó que estamos a tratar já foi expandido.

    @:param no
    @:return true/false
    """

    def _ciclo(self, no):
        __noAux = no.antecessor
        while __noAux:
            if no.estado == __noAux.estado:
                return True
                       
            __noAux = __noAux.antecessor
        
        return False
