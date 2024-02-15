public class Main {
    public static long fibonacci(int n) {
        long[] fib = new long[n+1];
        fib[0] = 0;
        fib[1] = 1;
        for (int i = 2; i <= n; i++) {
            fib[i] = fib[i-1] + fib[i-2];
        }
        return fib[n];
    }
    public static void main(String[] args) {
        System.out.println(fibonacci(n));
    }
}
