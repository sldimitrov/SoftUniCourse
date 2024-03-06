import java.util.Scanner;

public class FourOperations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double x = scanner.nextDouble();
        double y = scanner.nextDouble();
        System.out.printf("%.2f + %.2f = %.2f%n", x, y, x + y);
        System.out.printf("%.2f - %.2f = %.2f%n", x, y, x - y);
        System.out.printf("%.2f * %.2f = %.2f%n", x, y, x * y);
        System.out.printf("%.2f / %.2f = %.2f%n", x, y , x / y);

    }
}
