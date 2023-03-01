public class CheckingAccount extends Account{
    private double credit;
    
    public CheckingAccount(){
        super(0.0,"");
        this.credit = 0;
    }
    public CheckingAccount(double balance, String name, double credit){
        super(balance,name);
        this.credit = credit;
    }
    public void setCredit(double credit){
        if(credit>0){
            this.credit = credit;
        }else{
            System.out.println("Input number must be a positive integer.");
        }
    }
    public double getCredit(){
        return this.credit;
    }
    
   
    public void withdraw(double a){
        if(a>0){
            
            if(getBalance()-a>0){
                setBalance(getBalance()-a);
                System.out.println(a+" baht is withdrawn from "+this.name+
                        " and your credit balance is "
                +this.credit);
           }else{
               System.out.println("Not enough money!");
           }
            }
        else if((getBalance()-a <0)&&(((getBalance()-a)+this.credit)>0)){
            setBalance(getBalance()-this.credit);
            setBalance(0);
            System.out.println(a+" baht is withdrawn from "+this.name+
                    " and your credit balance is "
                +this.credit+".");
        }
        else if((getBalance()-a <0)&&(((getBalance()-a)+this.credit)<0)){
            System.out.println("Not enough money!");
        }
    }
    
    public void withdraw(String a){
        if(Double.parseDouble(a)>0){
           
     
            if(getBalance()-Double.parseDouble(a) >0){
                setBalance(getBalance()-Double.parseDouble(a));
                System.out.println(a+" baht is withdrawn from "+this.name+
                        " and your credit balance is "
                +this.credit+".");
           }else{
               System.out.println("Not enough money!");
           }
            }
        else if((getBalance()-Double.parseDouble(a) <0)&&((getBalance()-Double.parseDouble(a))+this.credit)>0){
            setBalance(getBalance()-this.credit);
            setBalance(0);
             System.out.println(a+" baht is withdrawn from "+this.name+
                     " and your credit balance is "
                +this.credit);
        }
        else if((getBalance()-Double.parseDouble(a) <0)&&(((getBalance()-Double.parseDouble(a))+this.credit)<0)){
            System.out.println("Not enough money!");
        }
    }
   
    public String toString(){
        return "The"+getName()+" account has"+getBalance()+" baht and "+
                this.credit+"credits.";
    }

    
    
    
    }
    

