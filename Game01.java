class Players {
    public String name;
    public double HP;
    public double atk;
    public int lv;
    
    public void showDetail(){
        System.out.println("name : " + name);
        System.out.println("HP : " + HP);
        System.out.println("atk : " + atk);
        System.out.println("lv : " + lv);
    }
    public void attack(Monster m){
        int n = (int) m.HP;
        if(n-atk >= 0)
           m.HP -= atk;
        else
            m.HP = 0; 
    }
}

class Monster{
    public String name;
    public double HP;
    public double atk;
    public int lv;
    
    public void showDetail(){
        System.out.println("name : " + name);
        System.out.println("HP : " + HP);
        System.out.println("atk : " + atk);
        System.out.println("lv : " + lv);
    }
    public void attack(Players m){
        int n = (int) m.HP;
        if(n-atk >= 0)
            m.HP -= atk;
        else
            m.HP = 0;  
    }
}
public class Game01{
    public static void main(String[] args) {
        Players p1 = new Players();
        p1.name = "Alex";
        p1.HP = 1000;
        p1.atk = 20;
        p1.lv = 5;
        
        Monster m1 = new Monster();
        m1.name = "POO1";
        m1.HP = 100;
        m1.atk = 10;
        m1.lv = 3;
        
        Monster m2 = new Monster();
        m2.name = "POO2";
        m2.HP = 120;
        m2.atk = 12;
        m2.lv = 5;
        
        p1.attack(m1);
        p1.attack(m2);
        
        m1.attack(p1);
        m2.attack(p1);
        
        p1.showDetail();
        m1.showDetail();
        m2.showDetail();
        
    }
}
