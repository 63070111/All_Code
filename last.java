import java.util.*;
public class last {
    public static void main(String[] args) {
        int number, full = 0;
        Scanner value = new Scanner(System.in);
        number = value.nextInt();
        while(true)
        {
            number = value.nextInt();
            if(number == -1)
            {
                break;
            }
            else
            {
             full = number;   
            }
           
            
        }System.out.println(full);
        
            
        
    }
}
