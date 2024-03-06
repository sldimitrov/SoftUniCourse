import java.util.Scanner;

public class BonusPoints {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int points = sc.nextInt();

        if (points <= 0 && points <= 3)
            points += 3;
        else if (points >= 4 && points <= 6)
            points += 15;
        else if (points >= 7 && points <= 9)
            points += 20;
        System.out.println(points);

    }
}
