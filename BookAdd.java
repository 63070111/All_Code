import javax.swing.*;
import java.awt.*;

public class BookAdd {
    private JFrame fr;
    private JLabel lb1, lb2, lb3;
    private JTextField tf1, tf2;
    private JComboBox cb;
    private JButton btn;
    private JPanel pn, pn2;

    public JButton getBtn() {
        return btn;
    }

    public JFrame getFr() {
        return fr;
    }

    public JTextField getTf1() {
        return tf1;
    }

    public JTextField getTf2() {
        return tf2;
    }

    public JComboBox getCb() {
        return cb;
    }

    public BookAdd() {
        fr = new JFrame();
        lb1 = new JLabel("Name");
        lb2 = new JLabel("Price");
        lb3 = new JLabel("Type");
        tf1 = new JTextField();
        tf2 = new JTextField();
        btn = new JButton("Insert");
        cb = new JComboBox();
        pn = new JPanel();
        pn2 = new JPanel();
        
        pn.setLayout(new GridLayout(3,2));//วางส่วนเพิ่ม name price id
        pn.add(lb1);//JLabel
        pn.add(tf1);//JTextField
        pn.add(lb2);//JLabel
        pn.add(tf2);//JTextField
        pn.add(lb3);//JLabel
        pn.add(cb);//JTextField
        cb.addItem("General");
        cb.addItem("Computer");
        cb.addItem("Math&Sci");
        cb.addItem("Photo3");
        
        pn2.setLayout(new FlowLayout());//JButton
        pn2.add(btn);
        
        fr.setLayout(new BorderLayout());//mix
        fr.add(pn, BorderLayout.CENTER);
        fr.add(pn2, BorderLayout.SOUTH);
        
        fr.pack();
        fr.setVisible(true);
        fr.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
    }
}
