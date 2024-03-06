import java.util.Scanner;

public class FindMinAndMax {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int biggest = Integer.MIN_VALUE;
        int smallest = Integer.MAX_VALUE;
        while(true) {
            String nextLine = scanner.nextLine();
            if (nextLine.equals("END"))
                break;
            int num = Integer.parseInt(nextLine);
                if (num > biggest) biggest = num;
                if (num < smallest) smallest = num;

        }
        System.out.println("Min number: " + smallest);
        System.out.println("Max number: " + biggest);
    }
}
