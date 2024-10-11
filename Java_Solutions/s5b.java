package Java_Solutions;

import java.io.File;

public class s5b {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("No file names provided!");
            return;
        }

        for (String fileName : args) {
            File file = new File(fileName);

            if (file.exists()) {
                if (fileName.endsWith(".txt")) {
                    boolean deleted = file.delete();
                    if (deleted) {
                        System.out.println("Deleted: " + fileName);
                    } else {
                        System.out.println("Could not delete: " + fileName);
                    }
                } else {
                    System.out.println("File Name: " + file.getName());
                    System.out.println("File Location: " + file.getAbsolutePath());
                    System.out.println("File Size: " + file.length() + " bytes");
                    System.out.println("-------------------------");
                }
            } else {
                System.out.println("File not found: " + fileName);
            }
        }
    }
}
