import java.util.Scanner;

public class Tiles {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double rectangleW = scanner.nextDouble();
        double rectangleH = scanner.nextDouble();
        double tilesWt = scanner.nextDouble();
        double tilesHt = scanner.nextDouble();

        var rectangleArea = (rectangleH * rectangleW) * 1.1;
        var tilesArea = tilesHt * tilesWt;
        var pieces = rectangleArea / tilesArea;
        System.out.printf("%.0f %n", pieces);
    }
}
