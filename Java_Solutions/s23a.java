package Java_Solutions;

import java.io.File;

public class s23a {
    public static void main(String[] args) {
        File file = new File("hidden.txt");
        if (file.exists()) {
            if (file.isHidden()) {
                System.out.println("The file is hidden.");
            } else {
                System.out.println("The file is not hidden.");
                System.out.println("File path: " + file.getAbsolutePath());
            }
        } else {
            System.out.println("The file does not exist.");
        }
    }
}
