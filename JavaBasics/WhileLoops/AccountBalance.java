import java.util.Scanner;

public class AccountBalance {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double balance = 0;
        while(true) {
            String nextLine = scanner.nextLine();
            if (nextLine.equals("End"))
                break;
            double num = Double.parseDouble(nextLine);
            balance += num;
            if (num > 0)
                System.out.printf("Increase: %.2f\n", num);
            else
                System.out.printf("Decrease: %.2f\n", -num);
        }
        System.out.printf("Balance: %.2f\n", balance);
    }
}