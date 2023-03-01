import java.util.*;
public class Line2 {
    public static void main(String[] args) {
        int number;
        Scanner value = new Scanner(System.in);
        number = value.nextInt();
        for(int x=1; x<=number ;x++)
        {
            if(x%5==0)
            {
                System.out.println("|");
            }
            else{
                System.out.print("|");
            }
        }
    }
    }