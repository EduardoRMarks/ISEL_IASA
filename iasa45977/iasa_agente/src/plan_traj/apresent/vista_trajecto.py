"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

class VistaProjecto():

    def mostrar(self, solucao, mecanismo_procura):
        print()

        print("Número de nós processados: " + str(mecanismo_procura.get_nos_processados))
        print("Número máximo em memória: " + str(mecanismo_procura.get_max_mem))

        print()
        
        if solucao:
            print("Há solução!")

            while no := solucao.remover():
                print(no.estado.localidade, " :", no.operador.__repr__())

        else:
            print("Não há solução")