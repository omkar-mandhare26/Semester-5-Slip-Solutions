package Java_Solutions.TYBBACA;

public class Teacher {
    int TID;
    String TName;
    String Subject;

    public Teacher(int TID, String TName, String Subject) {
        this.TID = TID;
        this.TName = TName;
        this.Subject = Subject;
    }

    public void disp() {
        if (Subject.equals("Java")) {
            System.out.println("Teacher ID: " + TID + ", Name: " + TName + ", Subject: " + Subject);
        }
    }

    protected void finalize() {
        System.out.println("Teacher object is destroyed");
    }
}
