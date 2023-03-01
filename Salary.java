import java.util.*;
public class Salary {
    public static void main(String[] args) {
        
        String name;
        int age, numDay1, numDay2, weight, salary, full;
        
        Scanner value = new Scanner(System.in);
        System.out.println("Please insert your name : ");
        System.out.println("Please insert your age : ");
        System.out.println("Please insert number of working days : ");
        System.out.println("Please insert number of absent days : ");
        System.out.println("Please insert your body weight : ");
        
        name = value.nextLine();
        age = value.nextInt();
        numDay1 = value.nextInt();
        numDay2 = value.nextInt();
        weight = value.nextInt();
        
        System.out.println("Hi, "+name);
        if((age>=21)&&(age<=30)){
            salary = (numDay1 * 300)-(numDay2*50);
            if((weight>=10) &&(weight<=60)){
                full = salary+5000;
                System.out.println("Your salary is "+salary+" Bath");
                System.out.println("Your salary and bonus is "+full+" Bath");
            }else if((weight>=61) &&(weight<=90)){
                full = salary+(5000-((weight-60)*10));
                System.out.println("Your salary is "+salary+" Bath");
                System.out.println("Your salary and bonus is "+full+" Bath");
            }else{
                System.out.println("Your salary is "+salary+" Bath");
            }
                
        }else if((age>=31)&&(age<=40)){
            salary = (numDay1 * 500)-(numDay2*50);
            if((weight>=10) &&(weight<=60)){
                full = salary+5000;
                System.out.println("Your salary is "+salary+" Bath");
                System.out.println("Your salary and bonus is "+full+" Bath");
            }else if((weight>=61) &&(weight<=90)){
                full = salary+(5000-((weight-60)*10));
                System.out.println("Your salary is "+salary+" Bath");
                System.out.println("Your salary and bonus is "+full+" Bath");
            }else{
                System.out.println("Your salary is "+salary+" Bath");
            }
            
        }else if((age>=41)&&(age<=50)){
            salary = (numDay1 * 1000)-(numDay2*25);
            if((weight>=10) &&(weight<=60)){
                full = salary+5000;
                System.out.println("Your salary is "+salary+" Bath");
                System.out.println("Your salary and bonus is "+full+" Bath");
            }else if((weight>=61) &&(weight<=90)){
                full = salary+(5000-((weight-60)*10));
                System.out.println("Your salary is "+salary+" Bath");
                System.out.println("Your salary and bonus is "+full+" Bath");
            }else{
                System.out.println("Your salary is "+salary+" Bath");
            }
            
        }else if((age>=51)&&(age<=60)){
            salary = (numDay1 * 3000);
            if((weight>=10) &&(weight<=60)){
                full = salary+5000;
                System.out.println("Your salary is "+salary+" Bath");
                System.out.println("Your salary and bonus is "+full+" Bath");
            }else if((weight>=61) &&(weight<=90)){
                full = salary+(5000-((weight-60)*10));
                System.out.println("Your salary is "+salary+" Bath");
                System.out.println("Your salary and bonus is "+full+" Bath");
            }else{
                System.out.println("Your salary is "+salary+" Bath");
            }
            
        }
    }
}
