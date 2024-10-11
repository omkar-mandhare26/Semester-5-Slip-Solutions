package Java_Solutions;

class armstrong {
    static int n;

    public static void getN(int num) {
        n = num;
    }

    void isArmstrong() {
        int sum = 0;
        int temp = n;
        while (temp > 0) {
            int r = temp % 10;
            sum += (r * r * r);
            temp /= 10;
        }

        if (sum == n) {
            System.out.println("Number is armstrong number");
        } else {
            System.out.println("Number is not an armstrong number");
        }
    }
}

public class s3a {
    public static void main(String[] args) {
        armstrong.getN(153);
        armstrong obj = new armstrong();

        obj.isArmstrong();
    }

}