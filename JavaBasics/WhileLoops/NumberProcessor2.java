import java.util.Scanner;

public class NumberProcessor2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        while(true) {
            String command = scanner.nextLine();
            if (command.equals("Inc")) number++;
            if (command.equals("Dec")) number--;
            if (command.equals("End")) break;
        }
        System.out.println(number);
    }
}
