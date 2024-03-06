import java.util.Scanner;

public class EqualPairs {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        double prevSum = 0;
        double maxDiff = 0;

        for (int i = 0; i < n; i++) {
            double num1 = scanner.nextDouble();
            double num2 = scanner.nextDouble();
            double sum = num1 + num2;
            if (i > 0) {
                double diff = Math.abs(prevSum - sum);
                if (diff > maxDiff)
                    maxDiff = diff;
            }
            prevSum = sum;
        }
        if (maxDiff == 0) {
            System.out.println("Yes, value=" + prevSum);
        } else {
            System.out.println("No, maxdiff=" + maxDiff);
        }

    }
}
