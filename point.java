import java.util.*;
public class point {
    public static void main(String[] args) {
        Scanner people1 = new Scanner(System.in);
        Scanner people2 = new Scanner(System.in);
        Scanner people3 = new Scanner(System.in);
        System.out.println("Input score is ");
        double P1, P2, P3, full;
        P1 = people1.nextDouble();
        P2 = people2.nextDouble();
        P3 = people3.nextDouble();
        full = P1 + P2 + P3;
        System.out.println("Average is "+ full);
    }
    
}
