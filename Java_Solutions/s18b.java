package Java_Solutions;

import java.io.*;

public class s18b {
    public static void main(String[] args) {
        try {
            FileInputStream fileInputStream = new FileInputStream("input.txt");
            FileOutputStream fileOutputStream = new FileOutputStream("target.txt");
            int val;

            while ((val = fileInputStream.read()) != -1) {
                char currentChar = (char) val;

                if (Character.isDigit(currentChar)) {
                    fileOutputStream.write('*');
                } else if (Character.isLowerCase(currentChar)) {
                    fileOutputStream.write(Character.toUpperCase(currentChar));
                } else if (Character.isUpperCase(currentChar)) {
                    fileOutputStream.write(Character.toLowerCase(currentChar));
                } else {
                    fileOutputStream.write(currentChar);
                }
            }

            System.out.println("Data copied successfully");
            fileInputStream.close();
            fileOutputStream.close();
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
