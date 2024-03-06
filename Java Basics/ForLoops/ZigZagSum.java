import java.util.Scanner;

public class ZigZagSum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int sum = 0;

        for (int i = 1; i <= number; i++) {
            int integer = scanner.nextInt();
            if (i % 2 == 1) {
                sum += integer;
            } else if (i % 2 == 0) {
                sum -= integer;
            }

        }
        System.out.println(sum);
    }
}
