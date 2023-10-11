"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from blocos.mod_prob.movimento import Movimento
from blocos.mod_prob.planeador_mov import PlaneadorMov
from blocos.mod_prob.vista_trajecto import VistaProjecto

def main():

    MOVIMENTOS = [
        Movimento("Desempilhar", 1),
        Movimento("Desempilhar", 2),
        Movimento("Empilhar", 1),
        Movimento("Empilhar", 2)
    ]

    PILHA_INI = [[2, 3, 1], [], []]
    PILHA_FIN = [[1, 2, 3], [], []]
    
    solucao, mec_proc = PlaneadorMov().planear(MOVIMENTOS, PILHA_INI, PILHA_FIN)
    VistaProjecto().mostrar(solucao, mec_proc)

if __name__ == "__main__":
    main()