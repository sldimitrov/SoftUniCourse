import java.util.Scanner;

public class ExamCountdown {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int days = scanner.nextInt();

        for (int i = days; i >= 1; i--) {
            System.out.printf("%s days before exam", i);
            System.out.println( );
        }
        System.out.println("Exam has come");
    }
}
