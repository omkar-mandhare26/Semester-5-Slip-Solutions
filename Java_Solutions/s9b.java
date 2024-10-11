package Java_Solutions;

import java.util.*;

class invalidDataException extends Exception {
    public invalidDataException(String message) {
        super(message);
    }
}

class validator {
    public static void validatePAN(String pan) throws invalidDataException {
        if (!pan.matches("[A-Z]{5}[0-9]{4}[A-Z]{1}")) {
            throw new invalidDataException("Invalid Data");
        }
    }

    public static void validateContactNo(String contactNo) throws invalidDataException {
        if (!contactNo.matches("[6-9][0-9]{9}")) {
            throw new invalidDataException("Invalid Data");
        }
    }
}

public class s9b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter PAN: ");
        String PAN = sc.next();

        System.out.print("Enter Mobile No: ");
        String contactNo = sc.next();

        sc.close();

        try {
            validator.validatePAN(PAN);
            validator.validateContactNo(contactNo);
            System.out.println("Valid Data");
        } catch (invalidDataException e) {
            System.out.println(e);
        }
    }
}