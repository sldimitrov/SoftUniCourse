import java.util.Scanner;

public class SpecialNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int originalNum = scanner.nextInt();
        int num = Math.abs(originalNum);
        boolean isSpecial = true;
        while (num > 0) {
            int lastDigit = num % 10;
            num = num / 10;
            if (lastDigit != 0 && originalNum % lastDigit != 0) {
                isSpecial = false;
                break;
            }
        }
        if (isSpecial)
            System.out.println(originalNum + " is special");
        else
            System.out.println(originalNum + " is not special");
    }
}
