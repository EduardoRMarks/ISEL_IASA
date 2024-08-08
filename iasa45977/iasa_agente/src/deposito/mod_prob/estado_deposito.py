"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.mod.estado import Estado


class EstadoDeposito(Estado):

    
    @property
    def deposito(self):
        return self._deposito
    
    
    def __init__(self, deposito):
        self._deposito = deposito


    def id_valor(self):
        return self._deposito.__hash__()

