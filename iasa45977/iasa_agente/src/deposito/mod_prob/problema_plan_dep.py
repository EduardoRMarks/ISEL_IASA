"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.deposito.mod_prob.estado_deposito import EstadoDeposito
from src.deposito.mod_prob.operador_deposito import OperadorDeposito
from src.lib.mod.problema.problema import Problema


class ProblemaPlanDep(Problema):

    def __init__(self, depositos, dep_inicial, dep_final):        
        super().__init__(EstadoDeposito(dep_inicial), [OperadorDeposito(deposito.deposito, 
                                                            deposito.quantidade) for deposito in depositos])
        
        self._dep_final = EstadoDeposito(dep_final)
    
    def objectivo(self, estado):
        return estado == self._dep_final