import java.util.Scanner;

public class MinAndMaxNum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int iteration = scanner.nextInt();
        double max_num = -100000;
        double min_num = 100000;

        for(int i = 1; i<=iteration; i++) {
            int number = scanner.nextInt();
            if (number > max_num)
                max_num = number;
            if (number < min_num)
                min_num = number;
        }
        System.out.printf("Min number: %.0f", min_num);
        System.out.println();
        System.out.printf("Max number: %.0f", max_num);
    }
}
