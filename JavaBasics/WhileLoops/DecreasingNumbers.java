import java.util.Scanner;

public class DecreasingNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        while (n >= 1) {
            System.out.println(n);
            n--;
        }
    }
}
