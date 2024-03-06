import java.util.Scanner;

public class Cinema {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String type = scanner.nextLine();
        int rows = scanner.nextInt();
        int seatsPerRow = scanner.nextInt();
        double price = 0;
        int seats = rows * seatsPerRow;
        double discount = 5 * seats;

        if (type.equals("Premiere")) {
            price = 12 * seats;
        } else if (type.equals("Normal")) {
            price = 7.5 * seats;
        } else {
            price = 5 * seats;
        }



        System.out.printf("%.2f", price);
    }
}
