import java.util.Scanner;

public class LetterCombinations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char startingLetter = scanner.nextLine().charAt(0);
        char endingLetter = scanner.nextLine().charAt(0);
        char excludedLetter = scanner.nextLine().charAt(0);

        int counter = 0;
        for (char l1 = startingLetter; l1 <= endingLetter; l1++) {
            for (char l2 = startingLetter; l2 <= endingLetter; l2++) {
                for (char l3 = startingLetter; l3 <= endingLetter; l3++) {
                    if (l1 != excludedLetter && l2 != excludedLetter && l3 != excludedLetter) {
                        System.out.print("" + l1 + l2 + l3 + " ");
                        counter += 1;
                    }
                }
            }
        }
        System.out.println(counter);
    }
}
