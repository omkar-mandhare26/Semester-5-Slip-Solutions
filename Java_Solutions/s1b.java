package Java_Solutions;

import java.io.*;

public class s1b {
    public static void main(String[] args) {
        try {
            FileReader reader = new FileReader("input.txt");
            FileWriter writer = new FileWriter("output.txt");
            int c;
            while ((c = reader.read()) != -1) {
                if (!Character.isDigit((char) c)) {
                    writer.write(c);
                }
            }
            reader.close();
            writer.close();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
