/**
 * IASA 22/23
 *
 * Trabalho realizado por:
 * Eduardo Marques 45977
 *
 * Docente Paulo Vieira
 */
package jogo.maqest;

import java.util.HashMap;

public class Estado <EV, AC> {

    String nome;
    HashMap<EV, Transicao<EV, AC>> transicoes;

    /**
     * Método construtor onde é criado o HashMap das transições
     * @param nome
     */

    public Estado(String nome){
        this.nome = nome;
        transicoes = new HashMap<EV, Transicao<EV, AC>>();
    }

    /**
     * Método que retorna o nome do estado em string
     * @return nome
     */
    public String getNome(){
        return nome;
    }

    /**
     * Método que retorna as transições a partir de um evento
     * @param EV
     * @return
     */
    public Transicao<EV, AC> processar(EV EV) {
        return transicoes.get(EV);
    }

    /**
     *  Método que chama o método transição para os eventos sem ação
     * @param EV
     * @param estadoSucessor
     * @return
     */
    public Estado<EV, AC> transicao (EV EV, Estado<EV, AC> estadoSucessor){
        return transicao(EV, estadoSucessor, null);
    }

    /**
     * Método que coloca o evento e a transicao no Hashmap transicoes
     * @param evento
     * @param estadoSucessor
     * @param accao
     * @return
     */
    public Estado<EV, AC> transicao (EV evento, Estado<EV, AC> estadoSucessor, AC accao){
        transicoes.put(evento, new Transicao<EV, AC>(estadoSucessor,  accao));
        return this;
    }
}
