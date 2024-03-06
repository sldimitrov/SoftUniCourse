import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        long sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
            System.out.print(i);
            if (i < n)
                System.out.print("+");
        }
        System.out.print("=" + sum);
    }
}