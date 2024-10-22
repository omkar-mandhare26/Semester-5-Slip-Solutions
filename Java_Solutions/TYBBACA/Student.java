package Java_Solutions.TYBBACA;

public class Student {
    int Rno;
    String SName;
    double Per;

    public Student(int Rno, String SName, double Per) {
        this.Rno = Rno;
        this.SName = SName;
        this.Per = Per;
    }

    public void disp() {
        System.out.println("Roll No: " + Rno + ", Name: " + SName + ", Percentage: " + Per);
    }

    protected void finalize() {
        System.out.println("Student object is destroyed");
    }
}
