import java.util.Scanner;

public class Sequence2k12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int maxNum = scanner.nextInt();
        int starter = 1;
        while(true) {
            if (starter > maxNum)
                break;
            System.out.println(starter);
            starter = starter * 2 + 1;
        }
    }
}
