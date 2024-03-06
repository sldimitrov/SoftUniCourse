import java.util.Scanner;

public class SumNNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        long sum = 0;

        for (int i=1; i<=n; i++) {
            double num = scanner.nextDouble();
            sum += num;
        }
        System.out.println(sum);
    }
}
