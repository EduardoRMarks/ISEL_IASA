"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

import math
from mod.agente.estado_agente import EstadoAgente
from mod.operador import Operador
from sae.agente.accao import Accao

"""
Classe OperadorMover que é um tipo de operador, logo herda da interface Operador.

Esta classe tem como objectivo a representação de um movimento que o agente do nosso problema pode executar
com a finalidade de se mover para uma dada posição. O seu movimento é obtido atrvés de uma translação deométrica
que será falada mais à frente nesta classe.
"""

class OperadorMover(Operador):

    """
    Propriedades read only.
    """

    @property
    def ang(self):
        return self._angulo
    
    @property
    def accao(self):
        return self._accao

    """
    Método construtor da classe OperadorMover.

    Este construtor recebe como parâmetros uma direção e o modelo mundo. Com a direção, instanciamos uma variável para
    guardar o ângulo da mesma e instanciamos uma accao do tipo Accao a partir da direção recebida. Guardamos o modelo 
    mundo recebido numa variável local para uso futuro.

    @:param direcao
    @:param modelo_mundo
    """

    def __init__(self, modelo_mundo, direcao):
        self._angulo = direcao.value
        self._accao = Accao(direcao)
        self._modelo_mundo = modelo_mundo

    """
    Método aplicar da classe OperadorMover,implementado a partir do método abstrato da interface Operador.

    Este método irá retornar, caso exista no domínio do modelo do mundo, um estado sucessor, estado esse que
    será o passo seguinte do nosso agente.

    Para tal, guardamos numa variável local a distancia, ou seja, o tamanho do passo do agente, chamamos o método
    translação, que nos irá indicar a posição do estado seguinte, inicializamos um novo EstadoAgente com a nova posição
    e, por fim, vamos verificar se o estado existe no domínio do modelo do mundo, como foi referido anteriormente
    retornando o novo estado caso a validação seja positiva.

    @:param estado
    @:return estado_suc
    """

    def aplicar(self, estado):
        distancia_passo = self._accao.passo
        posicao = estado.posicao
        nova_posicao = self.translacao(posicao, distancia_passo, self._angulo)
        estado_suc = EstadoAgente(nova_posicao)
        
        if estado_suc in self._modelo_mundo.obter_estados():
            return estado_suc
        
    """
    Método custo da classe OperadorMover,implementado a partir do método abstrato da interface Operador.

    Retorna o custa associado à aplicação do operador para obter o estado sucessor. O custo é porpocinal à distancia
    entre as posições, ou seja, quando mais longe as posições estiverem, maior o custo. O custo nunca é inferior a 1.

    @:param estado
    @:param estado_suc
    @:return custo
    """
    
    def custo(self, estado, estado_suc):
        return math.dist(estado.posicao, estado_suc.posicao)

    """
    Método translacao da classe OperadorMover.

    Este método tem como objectivo o cálculo da posição do estado sucessor do agente. Como o movimento do mesmo trata-se
    de uma translação geométrica, sabemos que, graças ao circulo trignométrico, um passo tem duas componentes, uma
    componente no eixo das abscissas e uma componente no eixo das ordenadas. Numa situação normal, para nos deslocarmos
    do ponto A ao ponto B teriamos de calcular B = Ax + dist*cos(ângulo), Ay + dist*sin(ângulo), mas como estamos a
    trabalhar num canvas, o eixo das ordenadas cresce de cima para baixc e não de baixo para cima. Ficamos assim com
    o seguinte calculo:

                     /B|
                    /  |
            dist ->/   | dy = -dist * sin(ângulo)
                  /    |
                A/-----|
                    dx = dist * cos(ângulo)

    O que significa que a posição B = Ax + dist*cos(ângulo), Ay + (-dist*sin(ângulo))

    @:param posicao
    @:param distancia
    @:param angulo
    @:return nova_posicao
    """
    
    def translacao(self, posicao, distancia, angulo):
        x, y = posicao
        dx = round(distancia * math.cos(angulo))
        dy = -round(distancia * math.sin(angulo))
        nova_posicao = x + dx, y + dy
        return nova_posicao