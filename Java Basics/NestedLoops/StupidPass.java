import java.util.Scanner;

public class StupidPass {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        for (int i = 2; i <= n ; i++) {
            for (int j = 1; j <= n ; j++) {
                if (i % 2 == 0 && j % 2 == 1)
                    System.out.printf("%d%d%d ", i, j, i * j);

            }
        }
    }
}
