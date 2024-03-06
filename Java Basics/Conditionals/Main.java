import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double num1 = scanner.nextDouble();
        double num2 = scanner.nextDouble();
        double num3 = scanner.nextDouble();

        if (num1 > num2 && num2 > num3) {
            System.out.println(num1);
        }
        if (num2 > num3 && num2 > num1) {
            System.out.println(num2);
        }
        if (num3 > num2 && num3 > num1) {
            System.out.println(num3);
        }
    }
}
