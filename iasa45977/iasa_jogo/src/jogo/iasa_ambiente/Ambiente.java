/**
 * IASA 22/23
 *
 * Trabalho realizado por:
 * Eduardo Marques 45977
 *
 * Docente Paulo Vieira
 */
package jogo.iasa_ambiente;

import java.util.Scanner;

/**
 * Classe do Meio Ambiente, onde teremos vários eventos e onde a personagem irá fazer uma certa ação escolhida pelo mesmo
 * */

public class Ambiente {

    Scanner keyboard =  new Scanner(System.in);

    private Evento evento;

    /**
     * Método que retorna o evento atual do ambiente
     * @return evento
     */
    public Evento getEvento(){
        return evento;
    }

    /**
     * Método que chamada o metodo "gerarEvento" e mostra o novo Evento escvolhido pelo utilizador
     */
    public void evoluir(){
        evento = gerarEvento();
        mostrar();
    }

    /**
     * Método que gera/atualiza um Evento a partir de uma letra inserida pelo utilizador.
     * O programa só avança quando o utilizador seleciona uma letra das utilizadas
     * @return novoEvento
     */
    private Evento gerarEvento(){
        Evento novoEvento = null;
        String comando;

        do {
            System.out.println("Gere um Evento do Ambiente (si, r, a, fu, fo) ou (t) para terminar");
            comando = keyboard.next();
            if (comando.equals("si")){
                novoEvento = Evento.SILENCIO;
            }
            if (comando.equals("r")){
                novoEvento = Evento.RUIDO;
            }
            if (comando.equals("a")){
                novoEvento = Evento.ANIMAL;
            }
            if (comando.equals("fu")){
                novoEvento = Evento.FUGA;
            }
            if (comando.equals("fo")){
                novoEvento = Evento.FOTOGRAFIA;
            }
            if (comando.equals("t")){
                novoEvento = Evento.TERMINAR;
            }
        }while (!comando.equals("si") && !comando.equals("r") && !comando.equals("a") && !comando.equals("fu") && !comando.equals("fo") && !comando.equals("t"));

        return novoEvento;
    }

    /**
     * Método que faz print do novo evento
     */
    private void mostrar(){
        System.out.println("Evento do ambiente:" + evento);
    }
}