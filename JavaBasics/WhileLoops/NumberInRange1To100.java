import java.util.Scanner;

public class NumberInRange1To100 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        while(number < 1 || number > 100) {
            System.out.println("Invalid number");
            number = scanner.nextInt();
        }
        System.out.println("Valid number");
        System.out.println(number);
    }
}
