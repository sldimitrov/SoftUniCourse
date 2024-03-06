import java.util.Scanner;

public class CheckforFoodorDrink {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String something = sc.nextLine();

        if (something.equals("curry") ||
                something.equals("noodles") ||
                something.equals("sushi") ||
                something.equals("spaghetti"))
                System.out.println("food");
        else if (something.equals("tea") ||
                something.equals("water") ||
                something.equals("coffee"))
                System.out.println("drink");
        else
            System.out.println("unknown");
    }
}

