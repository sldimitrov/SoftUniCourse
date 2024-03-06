import java.util.Scanner;

public class VacationExpenses {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String season = scanner.nextLine();
        String type = scanner.nextLine();
        int days = scanner.nextInt();
        double price = 0;

        if (type.equals("Hotel")) {
            if (season.equals("Spring"))
                price = 30 * 0.8;
            else if (season.equals("Summer"))
                price = 50;
            else if (season.equals("Autumn"))
                price = 20 * 0.7;
            else if (season.equals("Winter"))
                price = 40 * 0.9;

        } else if (type.equals("Camping"))
            if (season.equals("Spring"))
                price = 10 * 0.8;
            else if (season.equals("Summer"))
                price = 30;
            else if (season.equals("Autumn"))
                price = 15 * 0.7;
            else if (season.equals("Winter"))
                price = 10 * 0.9;
        System.out.printf("%.2f", price * days);
    }
}
