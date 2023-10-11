/**
 * IASA 22/23
 *
 * Trabalho realizado por:
 * Eduardo Marques 45977
 *
 * Docente Paulo Vieira
 */
package jogo.iasa_personagem;

import jogo.iasa_ambiente.Evento;
import jogo.maqest.Estado;
import jogo.maqest.MaquinaEstados;

/**
 * Classe onde é feito o controlo das ações da personagem
 * */

public class Controlo {

    MaquinaEstados maquinaEstados;
    Accao accao = null;

    Evento evento = null;

    /**
     * Método construtor onde criamos os 4 estados possíveis e onde atribuímos a cada estado as
     * prespectivas transições.
     * É também instanciada o construtor da máquina de estados
     */
    public Controlo() {
        Estado<Evento, Accao> procura =  new Estado<>("Procurar");
        Estado<Evento, Accao> inspeccao =  new Estado<>("Inspeccao");
        Estado<Evento, Accao> observacao =  new Estado<>("Observacao");
        Estado<Evento, Accao> registo =  new Estado<>("Registo");

        //Definir transições
        procura
                .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
                .transicao(Evento.RUIDO, inspeccao, Accao.APROXIMAR)
                .transicao(Evento.SILENCIO, procura, Accao.PROCURAR);

        inspeccao
                .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
                .transicao(Evento.RUIDO, inspeccao, Accao.PROCURAR)
                .transicao(Evento.SILENCIO, procura);

        observacao
                .transicao(Evento.FUGA, inspeccao)
                .transicao(Evento.ANIMAL, registo, Accao.OBSERVAR);

        registo
                .transicao(Evento.ANIMAL, registo, Accao.FOTOGRAFAR)
                .transicao(Evento.FUGA, procura)
                .transicao(Evento.FOTOGRAFIA, procura);

        maquinaEstados = new MaquinaEstados<>(procura);
    }

    /**
     * Método que retorna o estado atual
     * @return maquinaEstados.getEstado()
     */
    public Estado<Estado, Accao> getEstado(){
        return maquinaEstados.getEstado();
    }

    /**
     * Método que vai buscar o evento da percepcao da personagem, com a ação, utilizamos o método do processar
     * da classe MaquinaEstados com o evento da percepção para termos a ação exercida pela personagem. Por
     * último mostramos o estado e retornamos a ação
     * @param precepcao
     * @return
     */
    public Accao processar (Percepcao precepcao){
        evento = precepcao.getEvento();
        accao = (Accao) maquinaEstados.processar(evento);
        mostrar();
        return accao;
    }

    /**
     * Método que faz print do estado
     */
    private void mostrar(){
        System.out.println("Estado: " + getEstado().getNome());
    }
}
