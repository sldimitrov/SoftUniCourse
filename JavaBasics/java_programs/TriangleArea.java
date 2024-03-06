import java.util.Scanner;

public class TriangleArea {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double h = sc.nextDouble();
        double area = (a * h) / 2;
        System.out.printf("%.2f", area);
    }
}
