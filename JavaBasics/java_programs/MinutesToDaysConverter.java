import java.util.Scanner;

public class MinutesToDaysConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int minutes = sc.nextInt();
        int hours = minutes / 60;
        int days = hours / 24;
        System.out.println("Days are: " + days);
    }
}
