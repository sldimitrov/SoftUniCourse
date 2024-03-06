import java.util.Scanner;

public class MultiplicationTable {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();

        for (int i = 1; i <= 10; i++) {
            System.out.printf("%s x %s = %s", num, i, num * i);
            System.out.println();
        }

    }
}
