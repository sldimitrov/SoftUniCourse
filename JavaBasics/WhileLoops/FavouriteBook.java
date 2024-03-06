import java.util.Scanner;

public class FavouriteBook {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String favBook = scanner.nextLine();
        while (true) {
            String book = scanner.nextLine();
            if (book.equals(favBook)) {
                System.out.println("Book found!");
                break;
            }
            System.out.println("Invalid book: " + book);
        }
    }
}

