import java.util.Scanner;

public class ValidTriangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();

        if (a > b + c)
            System.out.println("Invalid Triangle");
        if (b > a + c)
            System.out.println("Invalid Triangle");
        if (c > b + a)
            System.out.println("Invalid Triangle");
        else
            System.out.println("Valid Triangle");
    }
}
