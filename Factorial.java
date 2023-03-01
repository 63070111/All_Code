import java.util.*;
public class Factorial {
    public static void main(String[] args) {
        int number,i = 1, f = 1,sum = 0;
        Scanner value = new Scanner(System.in);
        number = value.nextInt();
        while(i++ < number)
        {
            f *= i;
            sum = sum+f;
        }System.out.println(number +"! = " + sum);
    }
    
}
