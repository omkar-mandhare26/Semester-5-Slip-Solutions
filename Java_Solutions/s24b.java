package Java_Solutions;

import Java_Solutions.TYBBACA.*;
import java.util.Scanner;

public class s24b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of students: ");
        int n = sc.nextInt();
        Student[] students = new Student[n];

        for (int i = 0; i < n; i++) {
            System.out.println("Enter Roll No, Name, and Percentage for Student " + (i + 1) + ":");
            int rno = sc.nextInt();
            String name = sc.next();
            double per = sc.nextDouble();
            students[i] = new Student(rno, name, per);
        }

        System.out.println("\nStudent Details:");
        for (int i = 0; i < n; i++) {
            Student student = students[i];
            student.disp();
        }

        System.out.println("\nEnter the number of teachers: ");
        int m = sc.nextInt();
        Teacher[] teachers = new Teacher[m];

        for (int i = 0; i < m; i++) {
            System.out.println("Enter Teacher ID, Name, and Subject for Teacher " + (i + 1) + ":");
            int tid = sc.nextInt();
            String tname = sc.next();
            String subject = sc.next();
            teachers[i] = new Teacher(tid, tname, subject);
        }

        System.out.println("\nJava Teacher Details:");
        for (int i = 0; i < m; i++) {
            Teacher teacher = teachers[i];
            teacher.disp();
        }
        sc.close();
    }
}