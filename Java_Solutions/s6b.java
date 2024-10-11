package Java_Solutions;

public class s6b {
    public static void main(String[] args) {
        int[][] matrix = {
                { 74, 33, 65 },
                { 32, 4, 68 },
                { 69, 40, 78 } };

        final int m = 3;
        final int n = 3;
        int transpose[][] = new int[m][n];

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                transpose[j][i] = matrix[i][j];

        System.out.println("Original Matrix: ");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
                System.out.print(matrix[i][j] + "\t");
            System.out.println();
        }

        System.out.println("Transpose Matrix: ");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
                System.out.print(transpose[i][j] + "\t");
            System.out.println();
        }

    }
}
