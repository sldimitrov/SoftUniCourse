import java.util.Scanner;

public class Rollercoaster {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int places = scanner.nextInt();
        int ageLimit = scanner.nextInt();
        int n = scanner.nextInt();
        int placesFilled = 0;
        for (int i = 0; i < n; i++) {
            int childAge = scanner.nextInt();
            if (childAge >= ageLimit)
                placesFilled++;
        }
        if (placesFilled >= places)
            System.out.println("The rollercoaster departures");
        else
            System.out.println("Waiting...");
    }
}
