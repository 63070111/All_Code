import java.util.*;
public class Find {
    public static void main(String[] args) {
        Scanner value = new Scanner(System.in);
        int number,full1 = 0,full2=0;
        number = value.nextInt();
        while(number != -1)
        {
            number = value.nextInt();
            if(number%2 ==0){
                full1++;
            }
            else 
            {
                full2++;
            }
            
        }System.out.println("Odd number = "+full2+" Even number = "+full1);
    }
    
    
}
