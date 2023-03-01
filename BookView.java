import javax.swing.*;
import java.awt.*;

public class BookView {
    private JFrame fr, fr2;
    private JPanel pn1, pn2, pn3;
    private JLabel lb1, lb2, lb3;
    private JTextField tf1, tf2, tf3;
    private JButton btn1, btn2, btn3, btn4, btn5;
    private JComboBox cb;

    public JButton getBtn1() {
        return btn1;
    }

    public JButton getBtn2() {
        return btn2;
    }

    public JButton getBtn3() {
        return btn3;
    }

    public JButton getBtn4() {
        return btn4;
    }

    public JButton getBtn5() {
        return btn5;
    }

    public JTextField getTf1() {
        return tf1;
    }

    public JTextField getTf2() {
        return tf2;
    }

    public JTextField getTf3() {
        return tf3;
    }

    public JComboBox getCb() {
        return cb;
    }

    public JFrame getFr2() {
        return fr2;
    }

    public JFrame getFr() {
        return fr;
    }

    public BookView() {
        fr = new JFrame();
        fr2 = new JFrame();//สำหรับไว้แสดงตรงหน้าที่ให้กด OK
        pn1 = new JPanel();
        pn2 = new JPanel();
        pn3 = new JPanel();
        lb1 = new JLabel("Name");
        lb2 = new JLabel("Price");
        lb3 = new JLabel("Type");
        tf1 = new JTextField();
        tf2 = new JTextField();
        tf3 = new JTextField("0");
        btn1 = new JButton("<<<");
        btn2 = new JButton(">>>");
        btn3 = new JButton("Add");
        btn4 = new JButton("Update");
        btn5 = new JButton("Delete");
        cb = new JComboBox();
        
        pn1.setLayout(new GridLayout(3,2));//วางส่วนแรก name price id
        pn1.add(lb1);//JLabel
        pn1.add(tf1);//JTextField 
        pn1.add(lb2);//JLabel
        pn1.add(tf2);//JTextField 
        pn1.add(lb3);//JLabel
        pn1.add(cb);//JComboBox
        cb.addItem("General");
        cb.addItem("Computer");
        cb.addItem("Math&Sci");
        cb.addItem("Photo3");
        
        pn2.setLayout(new FlowLayout());//วางส่วน <<< number >>>
        pn2.add(btn1);//JButton
        pn2.add(tf3);//JTextField 
        pn2.add(btn2);//JButton
        
        pn3.setLayout(new FlowLayout());//วางส่วน add update delete
        pn3.add(btn3);//JButton
        pn3.add(btn4);//JButton
        pn3.add(btn5);//JButton
        
        fr.setLayout(new BorderLayout());//ประกอบ 3 ส่วน
        fr.add(pn1, BorderLayout.NORTH);
        fr.add(pn2, BorderLayout.CENTER);
        fr.add(pn3, BorderLayout.SOUTH);
        
        fr.pack();
        fr.setVisible(true);
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
