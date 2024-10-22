package Java_Solutions.Series;

public class Cube {
    public void printSeries(int n) {
        System.out.print("Cube of Numbers: ");
        for (int i = 1; i <= n; i++) {
            System.out.print((i * i * i) + " ");
        }
        System.out.println();
    }
}
