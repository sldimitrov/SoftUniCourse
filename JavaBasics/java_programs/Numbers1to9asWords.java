import java.sql.SQLOutput;
import java.util.Scanner;

public class Numbers1to9asWords {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();


        if (num == 1)
            System.out.printf("one");
        else if (num == 2)
            System.out.println("two");
        else if (num == 3)
            System.out.println("three");
        else if (num == 4)
            System.out.println("four");
        else if (num == 5)
            System.out.println("five");
        else if (num == 6)
            System.out.println("six");
        else if (num == 7)
            System.out.println("seven");
        else if (num == 8)
            System.out.println("eight");
        else if (num == 9)
            System.out.println("nine");
        else
            System.out.println("Out of range");
    }
}
