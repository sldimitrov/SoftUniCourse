import java.util.Scanner;

public class PowerOfNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double number = scanner.nextDouble();
        int p = scanner.nextInt();
        double result = 1;

        for(int i = 0; i < p; i++) {
            result = result * number;
        }
        System.out.printf("%.1f", result);
    }
}
