import java.util.Scanner;

public class USDToEUR {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double usd = scanner.nextDouble();
        double eur = usd * 0.88;
        System.out.printf("%.2f %n", eur);

    }
}
