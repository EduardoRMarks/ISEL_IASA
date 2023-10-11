"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""


from controlo_react.reaccoes.aproximar.estimulo.estimulo_alvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao

"""
Classe AproximarDir

É uma classe que herda da Classe Reaccao. Esta classe, quando deteta um alvo, tem um comportamentos de aproximação
em direção ao mesmo, dando um passo na sua direção.

Como é referido na classe AproximarAlvo, esta classe será instanciada 4 vezes, uma vez por cada direção no enumerado
Direccao. Sendo que a classe AproximarDir herda da classe Reaccao, iremos necessitar de um estimulo e de uma resposta.
Não pode qualquer estimulo devido à natureza do problema, assim, o estimulo será instanciado segundo a classe EstimuloAlvo, 
da mesma maneira que a resposta não pode ser uma resposta qualquer e sim uma resposta para uma direção.
"""


class AproximarDir(Reaccao):
    """
    Método construtor da classe AproximarDir, que chama o construtor da classe pai (Reaccao).

    O seu objetivo é, como o nome indica, apróximar-se de um alvo numa determinada direção. O construtor da classe Reaccao tem 
    como parâmetros de entrada um estímulo e uma resposta, então, a partir da direção recebida, teremos de instanciar um estimulo
    e uma resposta, usando as classes EstimuloAlvo e RespostaMover.

    @:param direccao
    """

    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))
