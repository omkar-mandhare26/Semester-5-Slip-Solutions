package Java_Solutions;

import java.util.*;

class numberException extends Exception {
    public String toString() {
        return "Error! Number is 0";
    }
}

class checkNum {
    static int n;

    public static void addition() {
        int temp = n;
        int lastDigit = temp % 10;
        int rev = 0;
        while (temp > 0) {
            int r = temp % 10;
            rev = (rev * 10) + r;
            temp /= 10;
        }
        int firstDigit = rev % 10;

        System.out.println("Sum of First Digit and Last Digit: " + (firstDigit + lastDigit));
    }

    static public void TwoSum() {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter any Integer: ");
        n = input.nextInt();
        input.close();

        try {
            if (n == 0)
                throw new numberException();
            else
                addition();
        } catch (numberException e) {
            System.out.println(e);
        }
    }
}

public class s6a {
    public static void main(String[] args) {
        checkNum.TwoSum();
    }
}
