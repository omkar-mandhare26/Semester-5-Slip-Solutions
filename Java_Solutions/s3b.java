package Java_Solutions;

import java.lang.Math;

abstract class Shape {
    abstract void area();

    abstract void volume();

    double PI = 3.1415;
}

class Cone extends Shape {
    public int r;
    public int h;

    Cone(int r, int h) {
        this.r = r;
        this.h = h;
    }

    public void area() {
        double area = PI * r * (r + (Math.sqrt(h * h + r * r)));
        System.out.println("Area of Cone: " + area);
    }

    public void volume() {
        double volume = PI * r * r * (h / 3);
        System.out.println("Volume of Cone: " + volume);
    }

}

class Cylinder extends Shape {
    public int r;
    public int h;

    Cylinder(int r, int h) {
        this.r = r;
        this.h = h;
    }

    public void area() {
        double area = (2 * PI * r * h) * 2 * PI * r * r;
        System.out.println("Area of Cylinder: " + area);
    }

    public void volume() {
        double volume = PI * r * r * h;
        System.out.println("Volume of Cylinder: " + volume);
    }

}

public class s3b {
    public static void main(String[] args) {
        Cone cone = new Cone(5, 7);
        cone.area();
        cone.volume();
        Cylinder cylinder = new Cylinder(5, 7);
        cylinder.area();
        cylinder.volume();
    }
}
