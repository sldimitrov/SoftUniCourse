import java.util.Scanner;

public class SumNumbersUntilStopped {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long sum = 0;

        for(;;) {
            int number = scanner.nextInt();
            if (number == 0)
                break;
            sum += number;
            System.out.println("Sum = " + sum);
        }
        System.out.println("Good bye");
    }
}
