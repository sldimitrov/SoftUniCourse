import java.util.Scanner;

public class UniquePinCodes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int max1 = scanner.nextInt();
        int max2 = scanner.nextInt();
        int max3 = scanner.nextInt();
        for (int i = 1; i <= max1; i++) {
            for (int j = 1; j <= max2; j++) {
                if (j == 2 || j == 3 || j == 5 || j == 7) {
                    for (int k = 1; k <= max3; k++) {
                        if (i % 2 == 0 && k % 2 == 0) {
                            System.out.printf("%d%d%d ", i, j, k);
                            System.out.println();
                        }
                    }
                }
            }
        }
    }
}
