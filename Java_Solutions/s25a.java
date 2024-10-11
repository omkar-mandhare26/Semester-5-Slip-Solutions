package Java_Solutions;

public class s25a {
    public static void main(String[] args) {
        String str = "level";
        boolean flag = true;
        int LP = 0;
        int RP = str.length() - 1;
        while (LP <= RP) {
            if (str.charAt(LP) != str.charAt(RP)) {
                flag = false;
                break;
            } else {
                LP++;
                RP--;
            }
        }

        if (flag) {
            System.out.println("String is Palindrome");
        } else {
            System.out.println("String is not Palindrome");
        }
    }
}
