/**
 * IASA 22/23
 *
 * Trabalho realizado por:
 * Eduardo Marques 45977
 *
 * Docente Paulo Vieira
 */
package jogo.maqest;

public class MaquinaEstados<EV, AC> {
    private Estado<EV, AC> estado;

    private AC accao;
    private Transicao<EV, AC> transicao;

    /**
     * Método construtor com um estado inicial
     * @param estadoInicial
     */
    public MaquinaEstados(Estado<EV, AC> estadoInicial){
        this.estado = estadoInicial;
    }

    /**
     * Método que retorna o estado atual
     * @return
     */
    public Estado<EV, AC> getEstado() {
        return estado;
    }

    /**
     * Método que recebe um evento e processa o mesmo para "escolher" a acção certa
     * @param evento
     * @return
     */
    public AC processar(EV evento){
        transicao = estado.processar(evento);
        if(transicao != null){
            estado = transicao.getEstadoSucessor();
            accao = transicao.getAccao();
            return accao;
        }
        else {
            return null;
        }

    }
}
