"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

"""
Classe VistaProjecto.

Esta classe tem como objectivo mostrar a solução, todos os paços até se chegar à solução
bem como a sua dimenção, ou seja, nº de mudanças efectuadas neste caso, custo das mesmas,
complexidade temporal e complexidade espacial.
"""

class VistaProjecto():

    def mostrar(self, solucao, mecanismo_procura):

        custo = solucao[-1].custo

        print()

        array = []
        passos = []
        
        if solucao:
            print("Solução:")

            while no := solucao.remover():
                if no.operador:
                    array.append(no.operador)
                
                if no.estado:
                    passos.append(no.estado)

            print(str(passos[0]))
            aux=0
            for i in range(len(array)):
                aux+=1
                print(str(passos[aux]), ' ', str(array[i]))

            print()
            
            print("Dimesão: ", str(len(array)))
            print("Custo:", str(custo))

            print("Complexidade temporal: " + str(mecanismo_procura.get_max_mem))
            print("Complexidade espacial: " + str(mecanismo_procura.get_nos_processados))
            
        else:
            print("Não há solução")