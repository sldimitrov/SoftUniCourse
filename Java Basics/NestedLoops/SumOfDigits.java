import java.util.Scanner;

public class SumOfDigits {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sumOfDigits = 0;
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("End"))
                break;
            int num = Integer.parseInt(input);
            while (num > 0) {
                sumOfDigits += num % 10;
                num = num / 10;
            }
            System.out.println("Sum of digits: " + sumOfDigits);
            sumOfDigits = 0;
        }
        System.out.println("Goodbye");
    }
}
