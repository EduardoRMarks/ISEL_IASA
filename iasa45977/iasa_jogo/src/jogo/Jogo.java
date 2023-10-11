/**
 * IASA 22/23
 *
 * Trabalho realizado por:
 * Eduardo Marques 45977
 *
 * Docente Paulo Vieira
 */
package jogo;



import jogo.iasa_ambiente.Ambiente;
import jogo.iasa_ambiente.Evento;
import jogo.iasa_personagem.Personagem;

/**
 * Classe princial que corre o jogo
 * */
public class Jogo {

    private static Ambiente ambiente;
    private static Personagem personagem;

    /**
     * Método que executa o jogo enquanto o evento selecionado pelo utilizador não seja TERMINAR
     */
    private static void executar(){
        do{
            personagem.executar();
            ambiente.evoluir();
        }while (ambiente.getEvento() != Evento.TERMINAR);
    }

    /**
     * Classe main que cria um ambiente e uma nova personagem.
     * Chama a classe executar que executa o jogo
     * @param args
     */
    public static void main(String[] args) {
        ambiente = new Ambiente();
        personagem =  new Personagem(ambiente);
        executar();
    }
}