package Java_Solutions;

import java.util.*;

public class s13b {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter Name: ");
        String name = input.nextLine();
        input.close();

        System.out.println("Hello " + name.toUpperCase() + ",nice to meet you!");
    }
}
