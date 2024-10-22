package Java_Solutions;

import java.util.*;

public class s20b {
    public static void main(String[] args) {
        LinkedList<String> languages = new LinkedList<>();
        languages.add("CPP");
        languages.add("Java");
        languages.add("Python");
        languages.add("PHP");

        System.out.println("Displaying contents using Iterator:");
        Iterator<String> iterator = languages.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }

        System.out.println("\nDisplaying contents in reverse order using ListIterator:");
        ListIterator<String> listIterator = languages.listIterator(languages.size());
        while (listIterator.hasPrevious()) {
            System.out.println(listIterator.previous());
        }
    }
}
