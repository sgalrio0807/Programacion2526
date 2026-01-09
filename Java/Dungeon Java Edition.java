package unidad2.RepasoNavidad;

import java.util.Random;
import java.util.Scanner;

public class dungeonJavaEdition {
    static void main(String[] args) {
        int hp = 100;
        int hpMonstruo = 80;
        int mp = 20;
        Random random = new Random();
        Scanner nombre = new Scanner(System.in);
        System.out.print("Dame el nombre de tu héroe: ");
        String heroe = nombre.next();

        while (hp>0 && hpMonstruo>0){
            System.out.println(heroe+ ":" +hp+ "puntos de vida (HP) y" +mp+ "puntos de energía (MP).\n" +
                                        "Monstruo:" +hpMonstruo+ "puntos de vida (HP).");
            System.out.println("1. Ataque Básico: No consume energía. El daño será un valor aleatorio entre 7 y 12.\n" +
                                "2. Ataque Especial: Consume 5 puntos de energía. El daño será un valor aleatorio entre 15 y 25. (Solo si tiene energía suficiente).\n" +
                                "3. Curar: Consume 8 de energía y recupera 20 de vida.\n");

            Scanner ataques = new Scanner(System.in);
            System.out.print("Dame el ataque que quieras hacer: ");
            int ataque = ataques.nextInt();

            switch (ataque){
                case 1:
                    int ataque1 = random.nextInt(7,12);
                    hpMonstruo = hpMonstruo - ataque1;
                    break;
                case 2:
                    if (mp>=5){
                        int ataque2 = random.nextInt(15,25);
                        hpMonstruo = hpMonstruo - ataque2;
                        mp = mp - 5;
                        break;
                    }
                case 3:
                    if (mp>8){
                        System.out.print("Curación");
                        mp = mp - 8;
                        hp = hp + 20;
                        break;
                    }
            
            if (hpMonstruo>0){
                int ataquemonstruo = random.nextInt(5,15);
                hp = hp - ataquemonstruo;
            }   

        }
        }
        if (hp<= 0){
            System.out.print("Tu héroe ha muerto");
        }
        else if (mp<= 0){
            System.out.print("Tu héroe se ha quedado sin energía");
        }
        else if (hpMonstruo<= 0){
            System.out.print("El monstruo ha sido derrotado");
        }
    }
}
