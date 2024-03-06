import java.util.Scanner;

public class AccountBalance2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double balance = 0;
        while(true) {
            String nextLine = scanner.nextLine();
            if (nextLine.equals("End"))
                break;
            double payment = Double.parseDouble(nextLine);
            if (payment > 0) {
                balance += payment;
                System.out.printf("Increase: %.2f\n", payment);
            }else if (payment < 0) {
                balance += payment;
                System.out.printf("Decrease: %.2f\n", Math.abs(payment));
            }
        }
        System.out.printf("Balance: %.2f\n", balance);
    }
}
