import java.util.Scanner;

public class BoilingWater {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double temperature = scanner.nextDouble();

        if (temperature > 100)
            System.out.println("The water is boiling");
        else
            System.out.println("The water is not hot enough");
    }
}
