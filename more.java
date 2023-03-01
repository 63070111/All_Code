import java.util.*;
public class more {
    public static void main(String[] args) {
        Scanner value = new Scanner(System.in);
        int number = 0, full = 0;
        while(true)
        {
            number = value.nextInt();
            if(number == -1)
            {
                break;
            }
            else
            {
             if(full >= number)
             {
                 continue;
             }
             else
             {
                 full = number;
             }
            }
           
            
        }System.out.println(full);
    }
}
