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

public class Percepcao {
    private Evento evento;

    /**
     * Metodo contrutor da percepção
     * @param evento
     */
    public Percepcao(Evento evento){
        this.evento = evento;
    }

    /**
     * Método que retorna o evento da percepção
     * @return
     */
    public Evento getEvento(){
        return evento;
    }
}
