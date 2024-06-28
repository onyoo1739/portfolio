import java.util.HashMap;
import java.util.Scanner;

public class Main {
    private static final HashMap<Long, Integer> memo = new HashMap<>();

    public static int collatz(long n) {
        if (n == 1) return 0;

        if (memo.containsKey(n)) return memo.get(n);

        int steps = 0;
        long original = n;

        while (n != 1) {
            if (memo.containsKey(n)) {
                steps += memo.get(n);
                break;
            }

            if ((n & 1) == 0) {
                n >>= 1; // n을 2로 나누기 (비트 시프트 연산으로 최적화)
            } else {
                n = 3 * n + 1; // n이 홀수인 경우
            }
            steps++;
        }

        memo.put(original, steps);
        return steps;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        System.out.println(collatz(n));
        s.close();
    }
}
