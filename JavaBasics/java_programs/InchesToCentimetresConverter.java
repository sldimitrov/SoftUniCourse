import java.util.Scanner;

public class InchesToCentimetresConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double inches = sc.nextDouble();
        double cm = inches * 2.54;
        System.out.printf("%.2f inches = %.2f cm", inches, cm);
    }
}
