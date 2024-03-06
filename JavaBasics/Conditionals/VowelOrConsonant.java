import java.util.Scanner;

public class VowelOrConsonant {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        input = input.toLowerCase();
        char letter = input.charAt(0);
        if (letter == 'a' || letter == 'o' || letter == 'i' ||
                letter == 'u' || letter == 'e') {
            System.out.println("Vowel");
        } else {
            System.out.println("Consonant");
        }
    }
}

