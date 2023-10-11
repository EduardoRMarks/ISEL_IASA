"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
Classe ProcuraGarfo herdeira da classe MecanismoProcura.

Neste tipo de procura, existem estados repetidos. Assim, para eliminação de nós correspondentes a 
estados repetidos, é necessário verificar se um novo nó sucessor corresponde a um estado que já foi 
anteriormente explorado.

Para facilitar o processamento dos nós repetidos, pode ser mantida uma única memória de nós explorados.
"""

class ProcuraGrafo(MecanismoProcura):
    
    """
    Método _iniciar_memoria da classe ProcuraGarfo implementado à custa do método abstrato da classe
    MecanismoProcura que herda.

    Neste método é recebida a fronteira e inicializada a mesma, tal como é inicializada a lista de
    nós explorados, lista esta que é inicializada com 0 elementos.

    @:param fronteira
    """

    def _iniciar_memoria(self):
        self._explorados = {}
        super()._iniciar_memoria()
        

    """
    Método _memorizar da classe ProcuraGarfo implementado à custa do método abstrato da classe
    MecanismoProcura que herda.

    Neste método, caso o nó ainda não tenha sido explorado (conseguimos tal informação graças ao método
    _manter da classe onde nos encontramos), inserimos o nó à fronteira de exploração e inserimos também
    o nó à lista de nós já explorados.

    @:param no
    """

    def _memorizar(self, no):
        if self._manter(no):
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)
            self._maior_mem = max(len(self._explorados), self._maior_mem)
            
    
    """
    Método _manter da classe ProcuraGarfo.

    Este método auxiliar tem como objectivo verificar se um certo nó recebido não pertence à lista de nós
    já explorados. Caso não faça parte da lista, então retorna true, ou seja, mantemos o nó, caso contrário
    retornamos false pois o nó já foi explorado anteriormente.

    @:param no
    @:return true/false
    """

    def _manter(self, no):
        return no.estado not in self._explorados