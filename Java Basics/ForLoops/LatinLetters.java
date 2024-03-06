import java.util.Scanner;

public class LatinLetters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char startingLetter = scanner.nextLine().charAt(0);
        char endingLetter = scanner.nextLine().charAt(0);

        for (char i = startingLetter; i <= endingLetter; i++) {
            System.out.print(i);
            System.out.print(" ");
        }
    }
}
