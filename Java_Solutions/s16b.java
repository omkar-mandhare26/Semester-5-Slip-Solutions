package Java_Solutions;

import java.util.Scanner;

class Employee {
    String name;

    Employee(String name) {
        this.name = name;
    }

    public void display() {
        System.out.println(name);
    }
}

public class s16b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of employees: ");
        int n = sc.nextInt();
        Employee[] emp = new Employee[n];

        System.out.println("Enter the names of the employees: ");
        for (int i = 0; i < n; i++) {
            emp[i] = new Employee(sc.next());
        }
        for (int i = 0; i < n; i++) {
            emp[i].display();
        }
        sc.close();
    }
}
