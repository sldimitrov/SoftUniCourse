import java.util.Scanner;

public class FirstNNumbersSum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        long sum = 0;

        for (int i = 1; i <= n; i++) {
            sum += i;
            System.out.print(i);
            if (i == n) {
                System.out.println("=" + sum);
                break;
            }
            System.out.print("+");
        }
    }
}
