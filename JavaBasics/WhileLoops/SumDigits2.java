import java.util.Scanner;

public class SumDigits2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        long sum = 0;
        while(number > 0) {
            int lastDigit = number % 10;
            sum += lastDigit;
            number = number / 10;
        }
        System.out.println(sum);;
    }
}
