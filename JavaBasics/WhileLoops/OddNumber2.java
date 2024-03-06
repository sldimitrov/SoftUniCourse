import java.util.Scanner;

public class OddNumber2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        while (num % 2 == 0) {
            num = scanner.nextInt();
        }
        System.out.println(num);
    }
}
