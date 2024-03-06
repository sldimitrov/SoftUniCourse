import java.util.Scanner;

public class DaysToMinutesConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int days = sc.nextInt();
        int hours = days * 24;
        int minutes = hours * 60;
        System.out.println("Minutes are : " + minutes);
    }
}
