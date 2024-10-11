package Java_Solutions;

import java.util.*;

public class s13a {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Size of array: ");
        int n = input.nextInt();

        ArrayList<Integer> nums = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            System.out.print("Enter element " + (i + 1) + ": ");
            int num = input.nextInt();
            nums.add(num);
        }
        input.close();

        System.out.println("\nArray Elements:");
        for (int i = 0; i < nums.size(); i++) {
            System.out.print(nums.get(i) + " ");
        }
    }
}
