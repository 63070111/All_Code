import java.util.*;
public class Sample {
    public static void main(String[] args) {
        Scanner tube = new Scanner(System.in);
        int number = tube.nextInt();
        System.out.print(number);
        for(int sign = 1; sign<=number; sign++){
            System.out.print("=");
        }
        System.out.print("+");
    }
    
}
