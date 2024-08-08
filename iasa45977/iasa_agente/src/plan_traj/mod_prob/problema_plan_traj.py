"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.mod.problema.problema import Problema
from src.plan_traj.mod_prob.estado_localidade import EstadoLocalidade
from src.plan_traj.mod_prob.operador_ligacao import OperadorLigacao

"""
Classe ProblemaPlanTraj que extende de Problema.

Esta classe irá tratar do problema/cenário, que neste caso será a partir de uma certa localidade
vamos querer chegar a uma outra localidade, obtendo assim o seu trajecto.
"""

class ProblemaPlanTraj(Problema):

    """
    Método construtor da classe ProblemaPlanTraj.

    Neste construtor, é chamado o construtor da super classe, que recebe um estado inicial e operadores.
    O seu estado incial é obtido através da instanciação da classe EstadoLocalidade(), passando o
    parâmetro da localidade inicial.

    Para a lista de operações, é feito uma lista a partir da lista de ligações recebida, a partir de um
    ciclo, criamos um uma lista de operadores, a partir dos 3 parâmetros presentes em cada ligação da
    lista recebida.

    Inicializamos por fim um estado final a partir da classe EstadoLocalidade() com o parâmetro loc_final
    recebido.

    @:param ligacoes
    @:param loc_inicial
    @:param loc_final
    """

    def __init__(self, ligacoes, loc_inicial, loc_final):        
        super().__init__(EstadoLocalidade(loc_inicial), [OperadorLigacao(ligacao.origem, ligacao.destino,
                                                                         ligacao.custo) for ligacao in ligacoes])
        
        self._estado_final = EstadoLocalidade(loc_final)

    """
    Método objectivo da classe ProblemaPlanTraj implementada a partir do método asbtrato da super classe.

    Retorna um booleano caso o estado recebido seja o estado final.

    @:param estado
    @:return true/false
    """
    
    def objectivo(self, estado):
        return estado == self._estado_final