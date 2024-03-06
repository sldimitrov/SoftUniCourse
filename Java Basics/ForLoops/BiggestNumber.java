import java.util.Scanner;

public class BiggestNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int iteration = scanner.nextInt();
        double max_num = -10000;

        for(int i = 1; i<=iteration; i++) {
            int number = scanner.nextInt();
            if (number > max_num)
                max_num = number;
        }
        System.out.printf("%.0f", max_num);
    }
}
