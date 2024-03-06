import java.util.Scanner;

public class Building {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int floors = scanner.nextInt();
        int rooms = scanner.nextInt();
        for (int i = floors; i >= 1 ; i--) {
            for (int j = 0; j < rooms ; j++) {
                if (i == floors)
                    System.out.printf("L%d%d ", i, j);
                else if (i % 2 == 0)
                    System.out.printf("O%d%d ", i, j);
                else if (i % 2 == 1)
                    System.out.printf("A%d%d ", i, j);

            }
            System.out.println();
        }
    }
}
