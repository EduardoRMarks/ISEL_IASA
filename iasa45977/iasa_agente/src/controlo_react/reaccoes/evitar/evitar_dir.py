"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""


from controlo_react.reaccoes.evitar.estimulo.estimulo_obst import EstimuloObst
from ecr.reaccao import Reaccao

"""
Classe EvitarDir

É uma classe que herda da Classe Reaccao. Esta classe, quando detecta um obtaculo, tem um comportamento
de "fuga", ou seja, vai andar noutra direção.

Como é referido na classe EvitarObst, esta classe será instanciada 4 vezes, uma vez por cada direção no enumerado
Direccao. Sendo que a classe EvitarDir herda da classe Reaccao, iremos necessitar de um estimulo e de uma resposta, resposta
essa já recebida vinda da classe EvitarObst. Não pode qualquer estimulo devido à natureza do problema, assim, o estimulo será 
instanciado segundo a classe EstimuloObst.
"""


class EvitarDir(Reaccao):
    """
    Método construtor da classe EvitarDir, que chama o construtor da classe pai (Reaccao).

    O seu objetivo é, como o nome indica, evitar um obstaculo numa determinada direção. O construtor da classe Reaccao tem 
    como parâmetros de entrada um estímulo e uma resposta, então, a partir da direção recebida, teremos de instanciar um estimulo,
    classe EstimuloObst, e a resposta é a mesma recebida durante a instanciação.
    
    @:param direccao
    @:param resposta
    """

    def __init__(self, direccao, resposta):
        super().__init__(EstimuloObst(direccao), resposta)
