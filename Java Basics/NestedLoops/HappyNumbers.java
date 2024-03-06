import java.util.Scanner;

public class HappyNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n1 = scanner.nextInt();

        for (int i = 1; i <= 9; i++) {
            for (int j = 0; j <= 9; j++) {
                if (i + j == n1) {
                    for (int k = 0; k <= 9; k++) {
                        for (int l = 0; l <= 9; l++) {
                            if (k + l == n1) {
                                System.out.printf("%d%d%d%d ", i, j, k, l);
                            }
                        }
                    }
                }
            }
        }
    }
}