"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod
from src.lib.pee.mec_proc.no import No
from src.lib.pee.mec_proc.solucao import Solucao

"""
Classe abstrata MecanismoProcura

Esta classe estará encarregue de fazer a exploração do espaço de estados até encontrar
o objectivo para o problema.
"""

class MecanismoProcura(ABC):

    """
    Método construtor da classe MecanismoProcura.

    O construtor recebe uma fronteira e inicializa a mesma.

    @:param fronteira
    """

    def __init__(self, fronteira):
        self._fronteira = fronteira
        self._maior_mem = 0
        self._nos_processados = 0
    
    """
    Método iniciar a memória da classe MecanismoProcura.

    Inicializa a fronteira vazia.
    """
    def _iniciar_memoria(self):
        self._fronteira.iniciar()
    """
    Método abstrato memorizar da classe MecanismoProcura que irá ser implementada pela
    classe que dela herdar.

    Irá memorizar um nó.

    @:param no
    """

    @abstractmethod
    def _memorizar(self, no):
        pass

    """
    Método procurar da classe MecanismoProcura.

    O processo de procura ocorre por exploração do espaço de estados a partir do estado inicial. O espaço 
    de estados é representado como um grafo, onde cada vértice corresponde a um estado e cada arco 
    corresponde a uma transição entre estados.

    O processamento é realizado nos seguintes passos:
        - É verificado se o estado actual corresponde ao objectivo (se corresponder ao objectivo, o processamento 
        termina e é retornado o percurso (sequência de estados e operadores) do estado inicial ao estado objectivo);
        - Não sendo o estado actual um objectivo, esse estado é expandido, sendo gerados todos os estados sucessores 
        por aplicação dos vários operadores possíveis;
        - Para cada estado sucessor é repetido o processo;
        - Se não existirem estados sucessores, o processo de procura termina com a indicação de que não existe solução;

    Para manter a informação gerada em cada passo de procura é mantida uma estrutura de informação, designada árvore de 
    procura, que consiste numa estrutura em árvore, organizada em nós, que mantém informação relativa a cada transição 
    de estado explorada, relacionando cada nó com o seu antecessor e mantendo informação do estado correspondente ao nó 
    e do operador que originou a transição de estado respectiva gerando esse novo estado.
        
    @:param problema
    @:return Solucao
    """

    def procurar(self, problema):    
        no = No(problema.estado_inicial)
        self._iniciar_memoria()
        self._fronteira.inserir(no)
       
        while not self._fronteira.vazia:    
            no = self._fronteira.remover()

            if problema.objectivo(no.estado):
                return Solucao(no)
            else:
                self._nos_processados += 1
                for no_suc in self._expandir(problema, no):
                    self._memorizar(no_suc)

        
    """
    Método expandir da classe MecanismoProcura

    Tem como objectivo a expanção de um no quando nele são aplicados os operadores
    de um problema. Ficamos assim com novos nós "filhos" do nó original.

    Para tal é feito um ciclo for para cada operador do problema.

    @:param problema
    @:param no
    @:return lista de nós
    """

    def _expandir(self, problema, no):
        for operador in problema.operadores:
            est_suc = operador.aplicar(no.estado)
            if est_suc:
                yield No(est_suc, operador, no)

    """
    Método que retorna o valor da maior fronteira
    """

    @property
    def get_max_mem(self):
        return self._maior_mem
    
    """
    Método que retorna o valor de nós processados
    """

    @property
    def get_nos_processados(self):
        return self._nos_processados
