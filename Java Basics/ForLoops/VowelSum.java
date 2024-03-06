import java.util.Scanner;

public class VowelSum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int points = 0;

        for(int i = 0; i<=n; i++) {
            String vowel = scanner.nextLine();
            if (vowel.equals("a"))
                points += 1;
            if (vowel.equals("e"))
                points += 2;
            if (vowel.equals("i"))
                points += 3;
            if (vowel.equals("o"))
                points += 4;
            if (vowel.equals("u"))
                points += 5;

        }
        System.out.println(points);
    }
}
