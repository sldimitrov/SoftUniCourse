import java.util.Scanner;

public class MinAndMax {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        while (true) {
            String nextLine = scanner.nextLine();
            if (nextLine.equals("END"))
                break;
            int number = Integer.parseInt(nextLine);
            if (number > max) max = number;
            if (number < min) min = number;
        }
        System.out.println("Min number: " + min);
        System.out.println("Max number: " + max);
    }
}
