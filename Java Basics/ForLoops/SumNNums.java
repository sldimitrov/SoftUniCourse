import java.util.Scanner;

public class SumNNums {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        double sum = 0;

        for (int i = 0; i < n; i ++) {
            double number = scanner.nextDouble();
            sum += number;
        }
        System.out.println(sum);
    }
}
