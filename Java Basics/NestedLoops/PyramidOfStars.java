import java.util.Scanner;

public class PyramidOfStars {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int row = 1; row <= 5; row++) {
            for (int i = 1; i <= row; i++) {
                System.out.printf("*");
            }
            System.out.println(" ");
        }
    }
}
