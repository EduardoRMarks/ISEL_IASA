"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

"""
Classe Solucao

Esta classe representa um percurso correspondente a uma solução de um problema, ou seja,
cria uma lista com todos nós referentes ao percurso.
"""

class Solucao():

    """
    Propriedade read only que retorna a dimensão do percurso
    """

    @property
    def dimensao(self):
        return len(self._percurso)
    
    """
    Método construtor da classe Solucao.

    O construtor recebe o no final e cria o percurso até ao nó raiz, caso o nó final não seja
    o próprio nó raiz. Assim cria uma lista onde coloca na última posição o nó final recebido,
    cria uma variável privada que irá guardar o nó anterior ao recebido e, caso exista um nó anterior,
    entra num ciclo while onde vai inserir na primeira posição da lista do percuso a variável nó
    anterior, vê se existe outro nó anterior ao que acabamos de inserir e caso haja repete o processo.
    Este ciclo acaba quando último nó a ser inserido for o nó raiz, o que significa que não tem nenhum
    nó anterior.

    @:param no_final
    """

    def __init__(self, no_final):
        self._percurso = []
        no = no_final

        while no:
            self._percurso.insert(0, no)
            no = no.antecessor


    """
    Método remover da classe Solucao.

    Este método remove o primeiro nó do percurso.

    @:return lista de nos sem o no removido
    """

    def remover(self):
        if self.dimensao > 0:
            return self._percurso.pop(0)

    """
    Método __iter__() da classe Solucao.
    
    O método iter devolve um iterador para um dado objecto. Neste caso,
    itera sobre o percuso de nós. É utilizado para suporte de instruções 
    do tipo for-each, por exemplo.

    @:return iterador de nós da solução
    """

    def __iter__(self):
        return iter(self._percurso)

    """
    Método __getitem__() da classe Solucao.

    O método getitem é utilizado para obter um objecto a partir de uma lista de
    objectos e do índice onde o objecto se encontra. Este método é normalmente
    utilizado com containers como listas, tuplos, etc...

    @:param index
    @:return nó
    """

    def __getitem__(self, index):
        return self._percurso[index]