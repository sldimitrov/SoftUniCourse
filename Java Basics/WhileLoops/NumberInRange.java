import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class NumberInRange {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        while (num < 1 || num > 100) {
            System.out.println("Invalid number");
            num = scanner.nextInt();
        }
        System.out.println("Valid number: " + num);
    }
}