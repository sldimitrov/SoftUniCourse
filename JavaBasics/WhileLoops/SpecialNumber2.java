import java.util.Scanner;

public class SpecialNumber2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numS = scanner.nextInt();
        boolean isSpecial = true;
        int realSNum = numS;
        while (true) {
            int lastDigit = numS % 10;
            numS = numS / 10;
            if (lastDigit != 0)
                if (realSNum % lastDigit != 0)
                    isSpecial = false;
                    break;
            }
        if (isSpecial)
            System.out.println(realSNum + " is special");
        else
            System.out.println(realSNum + " is not special");
        }
}

