import java.util.Scanner;
import java.util.concurrent.atomic.LongAccumulator;

public class SpecialBonus {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double numberS = scanner.nextDouble();
        double lastN = 0;
        while (true) {
            double num = scanner.nextDouble();
            if (num == numberS) {
                break;
            } else {
                num = num * 120 / 100;
                lastN = num;
            }
        }
        System.out.println(lastN);
    }
}

