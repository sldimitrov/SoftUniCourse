import java.util.Scanner;

public class Travelling {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String destination = scanner.nextLine();
        while (!destination.equals("End")) {
            String line = scanner.nextLine();
            double budget = Integer.parseInt(line);
            double savings = 0;
            while (budget > savings) {
                String input = scanner.nextLine();
                double sum = Integer.parseInt(input);
                savings += sum;
                System.out.printf("Collected: %.2f", savings);
                System.out.println();
            }
            System.out.println("Going to " + destination + "!");
            destination = scanner.nextLine();
        }
    }
}
