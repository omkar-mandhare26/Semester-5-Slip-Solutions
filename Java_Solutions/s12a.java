package Java_Solutions;

public class s12a {
    public static void main(String[] args) {
        String[] strArr = { "RAKMO", "NITRAM", "IICIVA" };
        for (int i = 0; i < strArr.length; i++) {
            StringBuilder tempS = new StringBuilder(strArr[i]);
            tempS.reverse();
            System.out.println(tempS.toString());
        }
    }
}