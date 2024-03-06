import java.util.Scanner;

class HelloWorld {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        double tomatoPrice = scanner.nextDouble();
        double tomatoQuantity = scanner.nextDouble();
        double cucumberPrice = scanner.nextDouble();
        double cucumberQuantity = scanner.nextDouble();



        double tomatoCost = tomatoPrice * tomatoQuantity;
        System.out.printf("Cost of tomatoes: %.2f%n", tomatoCost);
        double cucumberCost = cucumberPrice * cucumberQuantity;
        System.out.printf("Cost of cucumbers: %.2f%n", cucumberCost);
    }
}