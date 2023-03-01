import java.awt.*;
import javax.swing.*;
public class TellerGUI {
    private JFrame fr;
    private JPanel panel,panel0,panel01;
    private JLabel line1, line2;
    private JTextField tx1, tx2;
    private JButton b1, b2, b3;
    public TellerGUI(){
        fr = new JFrame("Teller GUI");
        panel = new JPanel();
        panel0 = new JPanel();
        panel01 = new JPanel();
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        line1 = new JLabel("Balance                         ");
        line2 = new JLabel("Amount                          ");
        tx1 = new JTextField("6000");
        tx1.setEditable(false);
        tx2 = new JTextField(" ",15);
        b1 = new JButton("Deposit");
        b2 = new JButton("Withdraw");
        b3 = new JButton("Exit");
        
        panel.setLayout(new GridLayout(2,2));
        panel.add(line1);
        panel.add(tx1);
        panel.add(line2);
        panel.add(tx2);
        
        panel0.setLayout(new FlowLayout());
        panel0.add(b1); 
        panel0.add(b2);
        panel0.add(b3);
        
        panel01.setLayout(new GridLayout(2,2));
        panel01.add(panel);
        panel01.add(panel0);
        fr.add(panel01);
        fr.pack();
        fr.setVisible(true);
    }
    public static void main(String[] args) {
        new TellerGUI();
    }
}
