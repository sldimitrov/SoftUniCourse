import javax.swing.plaf.synth.SynthUI;
import java.util.Scanner;

public class PrimeNum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int k = 0;
        int low = scanner.nextInt();
        int high = scanner.nextInt();
        for (int i = low; i < high; i++) {
            boolean isPrime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0)
                    isPrime = false;

            }
            if (isPrime)
                System.out.printf("%d ", i);
        }
    }
}
