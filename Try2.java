import java.util.*;
public class Try2 {
    public static void main(String[] args) {
        double x,y;
        Scanner value = new Scanner(System.in);
        x = value.nextDouble();
        y = value.nextDouble();
        if(((x>=1)&&(x<=10)) && ((y>=1)&&(y<=100)))
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
    }
}
