"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from plan_traj.apresent.vista_trajecto import VistaProjecto
from plan_traj.planeador.ligacao import Ligacao
from plan_traj.planeador.planeador_trajecto import PlaneadorTrajecto


def main():
    LIGACOES = [
        Ligacao("Loc-0", "Loc-2", 25),
        Ligacao("Loc-0", "Loc-1", 5),
        Ligacao("Loc-1", "Loc-3", 12),
        Ligacao("Loc-1", "Loc-6", 5),
        Ligacao("Loc-2", "Loc-4", 30),
        Ligacao("Loc-3", "Loc-2", 10),
        Ligacao("Loc-3", "Loc-5", 5),
        Ligacao("Loc-4", "Loc-3", 2),
        Ligacao("Loc-5", "Loc-6", 8),
        Ligacao("Loc-5", "Loc-4", 10),      
        Ligacao("Loc-6", "Loc-3", 15),

        ################
        
        Ligacao("Loc-0", "Loc-7", 7),
        Ligacao("Loc-2", "Loc-7", 5),
        Ligacao("Loc-2", "Loc-8", 15),
        Ligacao("Loc-5", "Loc-9", 1),
        Ligacao("Loc-7", "Loc-8", 15),
        Ligacao("Loc-8", "Loc-4", 25),
        Ligacao("Loc-9", "Loc-6", 2),
        Ligacao("Loc-9", "Loc-10", 2),
        Ligacao("Loc-10", "Loc-4", 2)

    ]

    LOC_INI = "Loc-0"
    LOC_FIN = "Loc-6"

    solucao, mec_proc = PlaneadorTrajecto().planear(LIGACOES, LOC_INI, LOC_FIN)

    VistaProjecto().mostrar(solucao, mec_proc)


if __name__ == "__main__":
    main()


