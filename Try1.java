import java.util.*;
public class Try1 {
    public static void main(String[] args) {
        double x;
        Scanner value = new Scanner(System.in);
        x = value.nextDouble();
        if((x>1)||(x<-1))
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
    }
    
}
