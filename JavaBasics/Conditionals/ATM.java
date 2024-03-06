import java.util.Scanner;

public class ATM {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double balance = scanner.nextDouble();
        double withdraw = scanner.nextDouble();
        double limit = scanner.nextDouble();

        if (withdraw < balance && withdraw < limit) {
            System.out.println("The withdraw was successful.");
        } else if (withdraw > limit) {
            System.out.println("The limit was exceeded.");
        } else if (withdraw > balance)
            System.out.println("Insufficient availability.");
    }
}
