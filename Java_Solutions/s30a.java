package Java_Solutions;

import java.util.*;

class ZeroNumberException extends Exception {
    public ZeroNumberException(String message) {
        super(message);
    }
}

public class s30a {
    public static boolean isPalindrome(int number) {
        int originalNumber = number;
        int reversedNumber = 0;
        while (number != 0) {
            int digit = number % 10;
            reversedNumber = reversedNumber * 10 + digit;
            number /= 10;
        }
        return originalNumber == reversedNumber;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter a number: ");
            String input = scanner.nextLine();

            int number = Integer.parseInt(input);

            if (number == 0) {
                throw new ZeroNumberException("Number is Zero.");
            }

            if (isPalindrome(number)) {
                System.out.println("The number is a palindrome.");
            } else {
                System.out.println("The number is not a palindrome.");
            }

        } catch (ZeroNumberException e) {
            System.out.println(e.getMessage());
        } catch (NumberFormatException e) {
            System.out.println("Number is Invalid.");
        } finally {
            scanner.close();
        }
    }
}
