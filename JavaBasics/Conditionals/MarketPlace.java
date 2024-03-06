import java.util.Scanner;

public class MarketPlace {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String product = scanner.nextLine();
        String day = scanner.nextLine();
        double price = 0;

        if (day.equals("Weekday")) {
            if (product.equals("Banana"))
                price = 2.5;
            else if (product.equals("Apple"))
                price = 1.3;
            else if (product.equals("Kiwi"))
                price = 2.2;
        } else if (day.equals("Weekend")) {
            if (product.equals("Banana"))
                price = 2.7;
            else if (product.equals("Apple"))
                price = 1.6;
            else if (product.equals("Kiwi"))
                price = 3;
        }
        System.out.printf("%.2f",price);
    }
}
