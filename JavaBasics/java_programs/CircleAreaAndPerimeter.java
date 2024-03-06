import java.util.Scanner;
// 3.1415926535897932384626433
public class CircleAreaAndPerimeter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double radius = sc.nextDouble();
        double P = radius * 3.1415926535897932384626433 * 2;
        double area = radius * radius * 3.1415926535897932384626433;

        System.out.printf("Perimeter : %.2f\n", P);
        System.out.printf("Area : %.2f", area);

    }
}
