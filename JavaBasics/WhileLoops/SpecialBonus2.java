import java.util.Scanner;

public class SpecialBonus2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int lastNum = 0;
        while(true) {
            int input = scanner.nextInt();
            if (input == num)
                break;
            else
                lastNum = input;
        }
        System.out.println(lastNum * 1.2);
    }
}
