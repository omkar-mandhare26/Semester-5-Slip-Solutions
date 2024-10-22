package Java_Solutions;

public class s16a {
    public static void main(String[] args) {
        int n = 12345;
        System.out.println(sumOfDigits(n));
    }

    static int sumOfDigits(int n) {
        if (n == 0)
            return 0;
        else
            return n % 10 + sumOfDigits(n / 10);
    }
}
