import java.util.Scanner;

public class NumbersEndingW7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();

        for (int i = 1; i <= num; i++) {
            if (i % 10 == 7)
                System.out.println(i);
        }
    }
}
