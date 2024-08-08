"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""
from src.blocos.mod_prob.vista_trajecto import VistaProjecto
from src.deposito.planeador.depesv import DepEsv
from src.deposito.planeador.planeador_deposito import PlaneadorDeposito


def main():

    DEPOSITOS = [
        DepEsv("Encher", 2),
        DepEsv("Encher", 3),
        DepEsv("Vazar", 2),
        DepEsv("Vazar", 2)
    ]
    
    VOL_INI = 0
    VOL_FIN = 9

    solucao, mec_proc = PlaneadorDeposito().planear(DEPOSITOS, VOL_INI, VOL_FIN)

    VistaProjecto().mostrar(solucao, mec_proc)


if __name__ == "__main__":
    main()


