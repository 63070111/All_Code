import java.awt.event.*;
import java.io.*;
import java.util.*;
import javax.swing.JOptionPane;

public class BookController implements WindowListener, ActionListener{
    private Book model;
    private BookView view;
    private BookAdd add;
    private int num = 0, end=0, index=0;
    private ArrayList<Book> al = new ArrayList<Book>();
    
    public BookController() {
        view = new BookView();
        model = new Book();
        
        view.getBtn1().addActionListener(this);
        view.getBtn2().addActionListener(this);
        view.getBtn3().addActionListener(this);
        view.getBtn4().addActionListener(this);
        view.getBtn5().addActionListener(this);
        view.getFr().addWindowListener(this);
    }
    public static void main(String[] args) {
        new BookController();
    }

    @Override
    public void actionPerformed(ActionEvent ae) {
        if(ae.getSource().equals(view.getBtn3())){//ปุ่ม add
            add = new BookAdd();
            add.getBtn().addActionListener(this);
        }
        else if(ae.getSource().equals(view.getBtn1())){//ปุ่ม <<<
            if(al.isEmpty()){//case empty
                
            }
            else if(num>1 && num<=end){//case between 1-last
                num -= 1;// loop delete number 1
                view.getTf3().setText(num+"");
                index -= 1;// loop delete index 1
                view.getTf1().setText(al.get(index).getName()+"");
                view.getTf2().setText(al.get(index).getPrice()+"");
                view.getCb().setSelectedItem(al.get(index).getType());
            }
            else if(num == 1 && index == 0){//case first
                view.getTf1().setText(al.get(index).getName()+"");
                view.getTf2().setText(al.get(index).getPrice()+"");
                view.getCb().setSelectedItem(al.get(index).getType());
            }
        }
        else if(ae.getSource().equals(view.getBtn2())){// ปุ่ม >>>
            if(al.isEmpty()){//case empty
                
            }
            else if(num == 0){//case number equal 0
                num += 1;//loop add number 1
                view.getTf3().setText(num+"");
                view.getTf1().setText(al.get(index).getName()+"");
                view.getTf2().setText(al.get(index).getPrice()+"");
                view.getCb().setSelectedItem(al.get(index).getType());
            }
            else if(num>=1 && num<end){//case between 1-last
                num += 1;//loop add number 1
                view.getTf3().setText(num+"");
                index += 1;//loop add index 1
                view.getTf1().setText(al.get(index).getName()+"");
                view.getTf2().setText(al.get(index).getPrice()+"");
                view.getCb().setSelectedItem(al.get(index).getType());
            }
        }
        else if(ae.getSource().equals(view.getBtn4())){//case update
            String name = view.getTf1().getText();
            double price = Double.parseDouble(view.getTf2().getText());
            String item = (String) view.getCb().getSelectedItem();
            
            al.set(index, new Book(name, price, item));//update new value in arrayList
            JOptionPane.showMessageDialog(view.getFr2(), "Done It.","Update Command",JOptionPane.INFORMATION_MESSAGE);
        }
        else if(ae.getSource().equals(view.getBtn5())){//case delete
            al.remove(index);//delete index
            JOptionPane.showMessageDialog(view.getFr2(), "Done It.","Delete Command",JOptionPane.INFORMATION_MESSAGE);
            if(al.isEmpty()){//if empty
                
            }
            else{
                if(num == 1){//number equal 1
                    view.getTf1().setText(al.get(index).getName()+"");//ให้ว่าง
                    view.getTf2().setText(al.get(index).getPrice()+"");//ให้ว่าง
                    view.getCb().setSelectedItem(al.get(index).getType());//ให้ว่าง
                    end = al.size();//ให้ว่าง
                }
                else{
                    num -= 1;//delete number
                    index -= 1;//delete index
                    view.getTf3().setText(num+"");
                    view.getTf1().setText(al.get(index).getName()+"");//ให้ว่าง
                    view.getTf2().setText(al.get(index).getPrice()+"");//ให้ว่าง
                    view.getCb().setSelectedItem(al.get(index).getType());//ให้ว่าง
                }
            }
        }
        else if(ae.getSource().equals(add.getBtn())){//button insert
            String name = add.getTf1().getText();
            double price = Double.parseDouble(add.getTf2().getText());
            String item = (String) add.getCb().getSelectedItem();

            al.add(new Book(name, price, item));//add value in arrayList
            
            end = al.size();
            add.getFr().dispose();
            JOptionPane.showMessageDialog(view.getFr2(), "Done It.","",JOptionPane.INFORMATION_MESSAGE);
        }
    }
    
    @Override
    public void windowOpened(WindowEvent we) {
        File f = new File("Book.data");
        if(f.exists()){
            try(FileInputStream fread = new FileInputStream("Book.data");
                    ObjectInputStream ois = new ObjectInputStream(fread);){
                al = (ArrayList<Book>) ois.readObject();
                end = al.size();
                }
            catch(Exception i){
                i.printStackTrace();
            }
        }
    }

    @Override
    public void windowClosing(WindowEvent we) {
        try(FileOutputStream fwrite = new FileOutputStream("Book.data");
                ObjectOutputStream oos = new ObjectOutputStream(fwrite);){
            if(al.isEmpty()){
                System.out.println(al.isEmpty());
            }
            else{
                oos.writeObject(al);
            }
        }
        catch(Exception i){
            i.printStackTrace();
        }
    }

    @Override
    public void windowClosed(WindowEvent we) {}

    @Override
    public void windowIconified(WindowEvent we) {}

    @Override
    public void windowDeiconified(WindowEvent we) {}

    @Override
    public void windowActivated(WindowEvent we) {}

    @Override
    public void windowDeactivated(WindowEvent we) {}

}
