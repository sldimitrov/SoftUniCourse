import java.util.Scanner;

public class BiggestOfFiveNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double num1 = scanner.nextDouble();
        double num2 = scanner.nextDouble();
        double num3 = scanner.nextDouble();
        double num4 = scanner.nextDouble();
        double num5 = scanner.nextDouble();

        if (num1 >= num2 && num1 >= num3 & num1 >= num4 && num1 >= num5) {
            System.out.printf("%.0f", num1);
        } else if (num2 >= num1 && num2 >= num3 & num2 >= num4 && num2 >= num5) {
            System.out.printf("%.0f", num2);
        } else if (num3 >= num2 && num3 >= num1 & num3 >= num4 && num3 >= num5) {
            System.out.printf("%.0f", num3);
        } else if (num4 >= num2 && num4 >= num3 & num4 >= num1 && num4 >= num5) {
            System.out.printf("%.0f", num4);
        } else if (num5 >= num2 && num5 >= num3 & num5 >= num4 && num5 >= num1) {
            System.out.printf("%.0f", num5);
        }
    }
}
