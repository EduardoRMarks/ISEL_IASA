from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.explorar.explorar import Explorar
from controlo_react.reaccoes.recolher import Recolher
from sae.simulador import Simulador

# ______________________________________________________________________
# Activação

# comportamento = Explorar()
comportamento = Recolher()
controlo = ControloReact(comportamento)
Simulador(1, controlo).executar()