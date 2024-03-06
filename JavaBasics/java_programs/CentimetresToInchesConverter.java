import java.util.Scanner;

public class CentimetresToInchesConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double cm = sc.nextDouble();
        double inches = cm / 2.54;
        System.out.printf("%.2f cm = %.2f inches", cm, inches);
    }
}
