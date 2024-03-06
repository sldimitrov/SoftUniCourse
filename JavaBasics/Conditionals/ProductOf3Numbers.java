import java.util.Scanner;

public class ProductOf3Numbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double product1 = scanner.nextDouble();
        double product2 = scanner.nextDouble();
        double product3 = scanner.nextDouble();

        double sum = product1 * product2 * product3;
        if (sum > 0)
            System.out.println("positive");
        else if (sum < 0)
            System.out.println("negative");
        else
            System.out.println("zero");
    }
}
