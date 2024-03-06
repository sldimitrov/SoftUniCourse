import java.util.Scanner;

public class TriangleOfStartWhileLoop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int line = 1;
        while (line <= n) {
            int stars = line;
            while (stars-- > 0) {
                System.out.print("*");
            }
            System.out.println();
            line++;
        }
    }
}
