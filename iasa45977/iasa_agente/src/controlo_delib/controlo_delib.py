"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""



from src.controlo_delib.mec_delib import MecDelib
from src.controlo_delib.modelo.modelo_mundo import ModeloMundo
from src.lib.sae.agente.controlo import Controlo

"""
Classe controloDelib (controlo deliberativo), é um tipo de controlo, ou seja, herda da classe Controlo.

Neste tipo de controlo, o raciocínio prático suporta o processo geral de tomada de decisão que determina
o comportamento do agente. O comportamento mencionado refere-se a quais as acções a realizar perante as
percepções obtidas e o estado do modelo interno do mundo. O processo geral de tomada de decisão e acção
ocorre de forma cíclica com os seguintes passos:

        1: Observação do mundo, que gera percepções
        2: Actualização do modelo do mundo, com base nas mesmas percepções
        3: Deliberação do que fazer, gerando um conjunto de objectivos
        4: Planeamento de como fazer, gerando um planos de acção
        5: Executar esse mesmo plano de acção

Este raciocinio tem, contudo, alguns problemas sendo eles os recursos computacionais limitados, pois um ciclo
com esta complexidade requer bastante poder compotacional, ou seja, requer bastante memória e tempo de computação.
Outro problema é se existir uma mudança no ambiente, o que pode levar a resultados não desejados. Por causa do
dinamismo, o algoritmo ainda tera que reavaliar as suas opções e, caso haja alguma mudança considerável no mundo,
haverá uma eventual mudança de planos.
"""

class ControloDelib(Controlo):

    """
    Método construtor da classe ControloDelib.

    Neste método construtor, inicializamos um atributo planeador da classe através do planeador recebido.
    Inicializamos também um objecto do tipo Modelo mundo e por fim uma lista vazia de objectivos para os
    quais o agente irá atingir.

    @:param planeador
    """

    def __init__(self, planeador):
        self._planeador = planeador
        self._mod_mundo = ModeloMundo()
        self._objectivos = []
        self._mec_delib = MecDelib(self._mod_mundo)

    """
    Método processar da classe ControloDelib.

    Este método trata do processo de tomada de decisão e acção mencionado no incio da classe.
    Começamos por observar o mundo, observação essa recebida através do parâmetro percepção recebido. Assimilamos,
    ou seja, atualizamos o modelo do mundo a partir da percepção recebida. Caso haja uma alteração no modelo do
    mundo, reconsideramos, ou seja, deliberamos e formamos um novo plano de acção e, por fim, executamos o mesmo, caso
    não hava nenhuma mudança no modelo mundo, apenas executamos o mesmo plano.

    @:param percepcao
    @:return accao
    """

    def processar(self, percepcao):
        self._assimilar(percepcao)

        if self._reconsiderar():
            self._deliberar()
            self._planear()

        self._mostrar()
        
        return self._executar()

    """
    Método assimilar da classe ControloDelib.

    Atualiza o modelo do mundo com a informação recebida através da percepção. Assim, actualiza a representção
    do modelo do mundo.

    @:param per (percepcao)
    """

    def _assimilar(self, percepcao):
        self._mod_mundo.actualizar(percepcao)

    """
    Método reconsiderar da classe ControloDelib.

    Este método tem como objectivo verificar se o modelo do mundo foi alterado retornando True ou False. Caso
    se verifique que o modelo do mundo foi alterado,o processo de tomada de decisão, como foi mencionado atrás,
    irá deliberar e planear uma nova acção, caso contrario apenas executa a ação.

    @:return true/false
    """

    def _reconsiderar(self):
        return self._mod_mundo.alterado or self._plano is None
    
    """
    Método deliberar da classe ControloDelib.

    O método deliberar não é mais do que a atualização da lista de objectivos, objectivos esses que, neste caso,
    são os elementos ALVO.
    """

    def _deliberar(self):
        self._objectivos = self._mec_delib.deliberar()
    
    """
    Método planear da classe ControloDelib.

    Este método tem como objectivo o planeamento de um novo plano de acção. Para tal, iremos confirmar que a lista
    de objectivos não se encontra vazia. Em caso positivo planeamos um novo plano.
    """

    def _planear(self):
        if self._objectivos:
            self._plano = self._planeador.planear(self._mod_mundo, self._objectivos)
        else:
            self._plano = None

    """
    Método executar da classe ControloDelib.

    Este método está encarregue de retornar uma acção caso o planeador tenha uma alguma acção para realizar.
    Caso não exista acção no estado atual do agente, não é retornado nada.

    @:return accao
    """

    def _executar(self):
        if self._plano:
            operador = self._plano.obter_accao(self._mod_mundo.obter_estado())
            if operador:
                return operador.accao
        

    """
    Método mostrar da classe ControloDelib.

    Este método irá mostrar o modelo do mundo, através do método mostrar da classe ModeloMundo,
    irá também mostrar o plano do agente até ao objectivo atual, bem como todos os estados do
    mundo.

    O canvas é limpo a cada iteração para que a vizualização seja vista de forma correcta.
    """

    def _mostrar(self):
        self.vista.limpar()
        self._mod_mundo.mostrar(self.vista)
        if self._plano:
            self._plano.mostrar(self.vista)
        if self._objectivos:
            self.vista.mostrar_estados(self._objectivos)
    