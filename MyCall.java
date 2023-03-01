import java.util.*;
public class MyCall {
    public static void main(String[] args) {
        int salary;
        double full;
        Scanner tube = new Scanner(System.in);
        System.out.println("Enter your salary: ");
        salary = tube.nextInt();
        if(salary>50000){
            full = salary*0.1;
            
        }else{
            full = salary*0.05;
            
        }System.out.println("Salary is "+full);
    }
    
}
