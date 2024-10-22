package Java_Solutions;

class Area {
    public void getArea(int r) {
        System.out.println("Area of Circle: " + (r * r));
    }

    public void getArea(int width, int length) {
        System.out.println("Area of Rectangle: " + (width * length));
    }

    public void getArea(int base, int height, boolean isTriangle) {
        if (isTriangle) {
            System.out.println("Area of Triangle: " + (0.5 * (base * height)));
        }
    }
}

public class s18a {
    public static void main(String[] args) {
        Area area = new Area();
        area.getArea(5);
        area.getArea(5, 5);
        area.getArea(5, 5, true);
    }
}
