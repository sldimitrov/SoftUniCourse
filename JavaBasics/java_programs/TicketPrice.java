import java.util.Scanner;

public class TicketPrice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String TicketType = scanner.nextLine();
        if (TicketType.equals("student")) {
            double price = 1;
            System.out.printf("$%.2f", price);
        }
        else if (TicketType.equals("regular")) {
            double price = 1.6;
            System.out.printf("$%.2f", price);
        }
        else
            System.out.println("Invalid ticket type!");
    }
}
