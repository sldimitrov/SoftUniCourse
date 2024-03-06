import java.util.Scanner;

public class Market {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double temperature = scanner.nextDouble();

        if (temperature < 0)
            System.out.println("Freezing weather!");
    }
}
