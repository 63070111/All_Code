import java.util.*;
public class First {
    public static void main(String[] args) {
        Scanner value = new Scanner(System.in);
        int number,full;
        number = value.nextInt();
        full = number;
        if((number%2 ==0)|| (number%3 ==0))
        {
            System.out.println(full);
        }
        
        else
        {    
            while(true)
        {
            number = value.nextInt();
            if(number%2 ==0){
                break;
            }
            else if(number%3 ==0){
                break;
            }
            
        }
        System.out.println(full);
    }
    
}
}
