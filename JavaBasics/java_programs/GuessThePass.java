import java.sql.SQLOutput;
import java.util.Scanner;

public class GuessThePass {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String pass = scanner.nextLine();

        if (pass.equals("s3cr3t!"))
            System.out.println("Welcome");
        else
            System.out.println("Wrong password!");

    }
}
