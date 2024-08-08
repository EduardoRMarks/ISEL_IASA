from src.controlo_react.controlo_react import ControloReact
from src.controlo_react.reaccoes.explorar.explorar import Explorar
from src.controlo_react.reaccoes.recolher import Recolher
from src.lib.sae import Simulador

# ______________________________________________________________________
# Activação

comportamento = Explorar()
#comportamento = Recolher()
controlo = ControloReact(comportamento)
Simulador(1, controlo).executar()