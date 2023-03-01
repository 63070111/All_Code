import java.awt.*;
import javax.swing.*;
public class SimpleCalGUI {
    private JFrame fr;
    private JPanel panel,panel00,panel01,panel02,panel03;
    private JTextField tx1, tx2, tx3;
    private JButton b1, b2, b3, b4;
    public SimpleCalGUI(){
        fr = new JFrame("เครื่องคิดเลข");
        panel = new JPanel();
        panel00 = new JPanel();
        panel01 = new JPanel();
        panel02 = new JPanel();
        panel03 = new JPanel();
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        tx1 = new JTextField(" ",30);
        tx2 = new JTextField(" ",30);
        tx3 = new JTextField(" ",30);
        b1 = new JButton("บวก");
        b2 = new JButton("ลบ");
        b3 = new JButton("คูณ");
        b4 = new JButton("หาร");
        
        panel.setLayout(new GridLayout(1,1));
        panel.add(tx1);
        
        panel03.setLayout(new GridLayout(1,1));
        panel03.add(tx2);
        
        panel01.setLayout(new FlowLayout());
        panel01.add(b1); 
        panel01.add(b2);
        panel01.add(b3);
        panel01.add(b4);
        
        panel00.setLayout(new GridLayout(1,1));
        panel00.add(tx3);
        
        panel02.setLayout(new GridLayout(4,1));
        panel02.add(panel);
        panel02.add(panel03);
        panel02.add(panel01);
        panel02.add(panel00);
        fr.add(panel02);
        fr.pack();
        fr.setVisible(true);

     }
    public static void main(String[] args) {
        new SimpleCalGUI();
    }
}
