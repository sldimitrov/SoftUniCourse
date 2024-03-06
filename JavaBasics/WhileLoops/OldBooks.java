import java.util.Scanner;

public class OldBooks {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String favBook = scanner.nextLine();
        while(true) {
            String book = scanner.nextLine();
            if (book.equals(favBook))
                break;
            System.out.println("Invalid book: " + book);
        }
        System.out.println("Book found!");
    }
}
