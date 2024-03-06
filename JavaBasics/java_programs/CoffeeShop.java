import java.util.Scanner;

public class CoffeeShop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double price = 0;
        var drinkType = scanner.nextLine();
        if (drinkType.equals("coffe")) {
            price = 1;
        }
        else if (drinkType.equals("tea")) {
            price = 0.6;
        }
        var Extra = scanner.nextLine();
        if (Extra.equals("sugar")) {
            price += 0.4;
        }
        System.out.printf("Final price: $%.2f", price);
    }
}
