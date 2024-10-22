package Java_Solutions;

public class s19a {
    public static void fib_series(int n) {
        int a = 0, b = 1, c = 0;
        for (int i = 0; i < n; i++) {
            System.out.println(c);
            c = a + b;
            a = b;
            b = c;
        }
    }

    public static void main(String[] args) {
        fib_series(10);
    }
}
