/**
 * IASA 22/23
 *
 * Trabalho realizado por:
 * Eduardo Marques 45977
 *
 * Docente Paulo Vieira
 */
package jogo.iasa_personagem;

import jogo.iasa_ambiente.Ambiente;
import jogo.iasa_ambiente.Evento;

/**
 * Classe da personagem que procura, inspeciona, observa e regista
 * */

public class Personagem {
    private Controlo controlo;
    private Ambiente ambiente;

    /**
     * Método construtor da personagem
     * @param ambiente
     */
    public Personagem(Ambiente ambiente){
        this.ambiente = ambiente;
        this.controlo =  new Controlo();
    }

    /**
     * Método que percepciona um novo evento e que atua a partir de uma ação processada pelo controlo
     */
    public void executar(){
        Percepcao percepcao = percepcionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);
    }

    /**
     * Método que percepciona um novo evento
     * @return new Percepcao(evento)
     */
    private Percepcao percepcionar(){
        Evento evento = ambiente.getEvento();
        return new Percepcao(evento);
    }

    /**
     * Método que faz uma print da ação caso não seja nula
     * @param accao
     */
    private void actuar(Accao accao){
        if (accao != null){
            System.out.println("Acção: " + accao);
        }
    }
}