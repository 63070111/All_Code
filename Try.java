import java.util.*;
public class Try {
    public static void main(String[] args) {
        int x;
        Scanner value = new Scanner(System.in);
        x = value.nextInt();
        if((x>= 3)&&(x<30))
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
    }
    
}
