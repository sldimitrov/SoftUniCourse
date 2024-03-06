import java.util.Scanner;

public class SpeedInfo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double speed = scanner.nextDouble();

        if (speed <= 30)
            System.out.println("Slow");
        else if (speed > 30)
            System.out.println("Fast");
    }
}
