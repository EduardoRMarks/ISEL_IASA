"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from deposito.mod_prob.estado_deposito import EstadoDeposito
from mod.operador import Operador


class OperadorDeposito(Operador):


    def __init__(self, tipo_de_op, quantidade):
        self._tipo_de_op = tipo_de_op
        self._quantidade = quantidade
    

    def aplicar(self, estado):

        if self._tipo_de_op == "Encher":
            return EstadoDeposito(estado.deposito + self._quantidade)
        else:
            return EstadoDeposito(estado.deposito - self._quantidade)


    def custo(self, estado, estado_suc):
        return (estado.deposito - estado_suc.deposito)**2
    

    def __repr__(self):
        return f'{self._tipo_de_op}({self._quantidade})'