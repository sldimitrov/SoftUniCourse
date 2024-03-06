import java.util.Scanner;

public class Sequence2k1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numberStop = scanner.nextInt();
        int changer = 1;
        while (true) {
            if (changer > numberStop) {
                break;

            } else
                System.out.println(changer);
                changer = changer * 2 + 1;
        }
    }
}

