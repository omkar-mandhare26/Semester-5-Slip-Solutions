package Java_Solutions;

interface Shape {
    abstract void area();
}

class Circle implements Shape {
    public final int r;

    Circle(int r) {
        this.r = r;
    }

    public void area() {
        System.out.println("Area of Circle: " + (r * r));
    }
}

class Sphere implements Shape {
    public final int r;

    Sphere(int r) {
        this.r = r;
    }

    public void area() {
        System.out.println("Area of Circle: " + (4 * 3.14 * r * r));
    }
}

public class s8a {
    public static void main(String[] args) {
        Circle circle = new Circle(5);
        Sphere sphere = new Sphere(8);

        circle.area();
        sphere.area();
    }
}
