package Java_Solutions;

import java.util.HashMap;
import java.util.Map;

public class s10a {
    public static void main(String[] args) {
        String str = "This is a String";

        Map<Character, Integer> count = new HashMap<>();

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (count.containsKey(ch))
                count.put(ch, count.get(ch) + 1);
            else
                count.put(ch, 1);
        }

        for (Map.Entry<Character, Integer> entry : count.entrySet())
            System.out.println(entry.getKey() + ": " + entry.getValue());
    }
}