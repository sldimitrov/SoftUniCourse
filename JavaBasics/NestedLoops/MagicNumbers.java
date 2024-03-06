import java.util.Scanner;

public class MagicNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j < 9; j++) {
                for (int k = 1; k < 9; k++) {
                    int product = i * j * k;
                    if (product == n)
                        System.out.printf("%d%d%d ", i, j, k);
                }
            }
        }
    }
}
