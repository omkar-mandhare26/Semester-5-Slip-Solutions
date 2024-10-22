package Java_Solutions;

import java.io.*;

public class s24a {
    public static void main(String[] args) {
        int digitCount = 0;
        int spaceCount = 0;
        int characterCount = 0;

        String inputFilePath = "input.txt";

        try (FileInputStream fileInputStream = new FileInputStream(inputFilePath)) {
            int val;

            while ((val = fileInputStream.read()) != -1) {
                char currentChar = (char) val;

                if (Character.isDigit(currentChar)) {
                    digitCount++;
                } else if (Character.isWhitespace(currentChar)) {
                    spaceCount++;
                } else {
                    characterCount++;
                }
            }

            System.out.println("Number of digits: " + digitCount);
            System.out.println("Number of spaces: " + spaceCount);
            System.out.println("Number of characters: " + characterCount);

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
