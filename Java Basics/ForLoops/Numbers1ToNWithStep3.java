import java.util.Scanner;

public class Numbers1ToNWithStep3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i = 1; i <= n; i+=3) {
            System.out.println(i);
        }
    }
}
