import java.util.Scanner;

public class AreaofFigures {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String FigureType = scanner.nextLine();
        if (FigureType.equals("circle")) {
            double radius = scanner.nextDouble();
            double area = (radius * radius) * 3.14159265359;
            System.out.printf("%.2f", area);
        }
        else if (FigureType.equals("square")) {
            double a = scanner.nextDouble();
            double area = a * a;
            System.out.printf("%.2f", area);
        }
        else if (FigureType.equals("rectangle")) {
            double a = scanner.nextDouble();
            double b = scanner.nextDouble();
            double area = a * b;
            System.out.printf("%.2f", area);
        }
    }
}
