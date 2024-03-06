import java.util.Scanner;

public class Divisionto2a3and4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        double d2 = 0;
        double d3 = 0;
        double d4 = 0;

        for (int i = 1; i <= count; i++) {
            int number = scanner.nextInt();
            if (number % 2 == 0)
                d2 += 1;
            if (number % 3 == 0)
                d3 += 1;
            if (number % 4 == 0)
                d4 += 1;
        }
        System.out.printf("%.2f",d2 / count * 100);
        System.out.println("%");
        System.out.printf("%.2f",d3 / count * 100);
        System.out.println("%");
        System.out.printf("%.2f",d4 / count * 100);
        System.out.println("%");
    }
}
