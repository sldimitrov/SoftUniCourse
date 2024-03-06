import java.util.Scanner;

public class NumberOperations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double num1 = Double.parseDouble(scanner.nextLine());
        double num2 = Double.parseDouble(scanner.nextLine());
        String operator = scanner.nextLine();
        if (operator.equals("+")) {
            System.out.printf("%.0f %s %.0f = %.2f\n", num1, operator, num2, num1 + num2);
        } else if (operator.equals("-")) {
            System.out.printf("%.0f %s %.0f = %.2f", num1, operator, num2, num1 - num2 );
        } else if (operator.equals("*")) {
            System.out.printf("%.0f %s %.0f = %.2f", num1, operator, num2, num1 * num2);
        } else if (operator.equals("/")) {
            System.out.printf("%.0f %s %.0f = %.2f", num1, operator, num2, num1 / num2);
        } else if (operator.equals("%")) {
            System.out.printf("%.0f %s %.0f = %.2f", num1, operator, num2, num1 % num2);
        }
    }
}