import java.util.Scanner;

public class main {
    public static void main (String[] args) {
        boolean descobriu = true;
        Scanner tentativa = new Scanner(System.in);
        String input;
        termo teste = new termo();
        while (descobriu) {
            System.out.println("Faça uma tentativa:\nA palavra deve ter 5 letras");
            input = tentativa.nextLine();
            descobriu = teste.jogar(input);
        }
        tentativa.close();
    }
}   