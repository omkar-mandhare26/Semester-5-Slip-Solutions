package Java_Solutions;

public class s2a {
    public static boolean isVowel(char ch) {
        ch = Character.toLowerCase(ch);
        char vowels[] = { 'a', 'e', 'i', 'o', 'u' };
        for (char vowel : vowels) {
            if (ch == vowel) {
                return true;
            }
        }
        return false;
    }

    public static void main(String args[]) {
        String str = "Avicii - Tim Bergling";
        for (int i = 0; i < str.length(); i++) {
            if (isVowel(str.charAt(i))) {
                System.out.println(str.charAt(i));
            }
        }
    }
}
