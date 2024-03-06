import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class NumberProcessor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = Integer.parseInt(scanner.nextLine());
        String command = scanner.nextLine();
        while (!command.equals("End")) {
            if (command.equals("Inc"))
                number++;
            else if (command.equals("Dec"))
                number--;
            else
                System.err.println("Invalid input");
            command = scanner.nextLine();
        }
        System.out.println(number);
    }
}