from sae import Controlo
from sae import Simulador


# ______________________________________________________________________
# Controlo de teste

class ControloTeste(Controlo):
    def processar(self, percepcao):
        print("processar")


# ______________________________________________________________________
# Activação

controlo = ControloTeste()

Simulador(1, controlo).executar()
