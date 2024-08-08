from src.controlo_delib.controlo_delib import ControloDelib
from src.lib.plan.plan_pdm.planeador_pdm import PlaneadorPDM
from src.lib.sae import Simulador

controlo = ControloDelib(PlaneadorPDM(gama=0.8, delta_max=2))
Simulador(2, controlo).executar()