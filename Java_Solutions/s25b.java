package Java_Solutions;

import Java_Solutions.Series.*;
import java.util.Scanner;

public class s25b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of terms: ");
        int n = sc.nextInt();

        Fibonacci fibonacci = new Fibonacci();
        Cube cube = new Cube();
        Square square = new Square();

        fibonacci.printSeries(n);
        cube.printSeries(n);
        square.printSeries(n);

        sc.close();
    }
}
