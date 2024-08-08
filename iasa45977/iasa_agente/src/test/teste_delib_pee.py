from src.controlo_delib.controlo_delib import ControloDelib
from src.lib.plan.plan_pee.planeador_pee import PlaneadorPEE
from src.lib.sae import Simulador

planeador = PlaneadorPEE()

"""
0 = Manhattan
1 = Euclidiana
outros nums = HeurDist
"""

planeador.definir_heuristica(1)
controlo = ControloDelib(planeador)
Simulador(1, controlo).executar()