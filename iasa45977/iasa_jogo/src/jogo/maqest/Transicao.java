/**
 * IASA 22/23
 *
 * Trabalho realizado por:
 * Eduardo Marques 45977
 *
 * Docente Paulo Vieira
 */
package jogo.maqest;

public class Transicao <EV, AC>{

    private Estado<EV, AC> estado;
    private AC accao;

    /**
     * Método construtor que recebe estadoSucessor e ação
     * @param estadoSucessor
     * @param accao
     */
    public Transicao(Estado<EV, AC> estadoSucessor, AC accao){
        this.estado = estadoSucessor;
        this.accao = accao;
    }

    /**
     * Método que retorna o estado sucessor
     * @return estado
     */
    public Estado<EV, AC> getEstadoSucessor(){
        return estado;
    }

    /**
     * Método que retorna a ação
     * @return accao
     */
    public AC getAccao(){
        return accao;
    }
}
