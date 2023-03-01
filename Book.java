import java.io.Serializable;

public class Book implements Serializable{
    //ตัว implements Serializable ไว้แปลง Obj เป็น Byte สำหรับส่งผ่านข้อมูลผ่านท่อ
    private String name;
    private double price;
    private String type;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Book() {
        this("",0,"");
    }

    public Book(String name, double price, String type) {
        this.name = name;
        this.price = price;
        this.type = type;
    }

}
