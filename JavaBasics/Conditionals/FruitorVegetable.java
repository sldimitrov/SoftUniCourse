import java.util.Scanner;

public class FruitorVegetable {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String something = scanner.nextLine();

        if (something.equals("banana") ||
                (something.equals("apple")) ||
                (something.equals("kiwi")) ||
                (something.equals("cherry")) ||
                (something.equals("lemon")) ||
                (something.equals("grapes")))
            System.out.println("fruit");
        else if (something.equals("cucumber") ||
                something.equals("pepper") ||
                something.equals("carrot"))
            System.out.println("vegetable");
        else
            System.out.println("unknown");

    }
}
