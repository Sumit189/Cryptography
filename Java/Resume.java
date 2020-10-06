import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
class CardListener implements ActionListener
{
public void actionPerformed(ActionEvent e)
{
if(e.getSource() == CardLayoutDemo.b1)
{

CardLayoutDemo.cl.first(CardLayoutDemo.p);
}
else if(e.getSource() == CardLayoutDemo.b2)
{
CardLayoutDemo.cl.previous(CardLayoutDemo.p);
}
else if(e.getActionCommand().equals("Image")){
        JFileChooser jc = new JFileChooser();
        jc.showOpenDialog(CardLayoutDemo.jf);
        String filepath = jc.getSelectedFile().getPath();
        CardLayoutDemo.l8.setIcon(new ImageIcon(new ImageIcon(filepath).getImage().getScaledInstance(200,200,Image.SCALE_DEFAULT)));
      //  CardLayoutDemo.l10.setIcon(new ImageIcon(new ImageIcon(filepath).getImage().getScaledInstance(200,200,Image.SCALE_DEFAULT)));
}
else if(e.getActionCommand().equals("Submit")){
    String [][] students = {
        {   CardLayoutDemo.jt1.getText().toString(),
            CardLayoutDemo.jt2.getText().toString(),
            CardLayoutDemo.jt3.getText().toString(),
            CardLayoutDemo.jt4.getText().toString(),
            CardLayoutDemo.jt5.getText().toString()
            }
        };
        
  
CardLayoutDemo.p1.setLayout(null);
String [] header = {"Name","CGPA","Qualification","Field","Contact No."};      // will be header
JTable jts = new JTable(students,header);
JScrollPane hsp = new JScrollPane(jts);
hsp.setBounds(5,300,685,60);
CardLayoutDemo.p1.add(hsp);
//CardLayoutDemo.l10.setIcon(new ImageIcon((CardLayoutDemo.l8.getIcon().getImage().getScaledInstance(200,200,Image.SCALE_DEFAULT)));
}
else if(e.getSource() == CardLayoutDemo.b3)
{
CardLayoutDemo.cl.next(CardLayoutDemo.p);
}
else if(e.getSource() == CardLayoutDemo.b4)
{
CardLayoutDemo.cl.last(CardLayoutDemo.p);
}
else if(e.getSource() == CardLayoutDemo.jcb)
{
CardLayoutDemo.cl.show(CardLayoutDemo.p, CardLayoutDemo.jcb.getItemAt(CardLayoutDemo.jcb.getSelectedIndex()));
}
}
}


class CardLayoutDemo
{
static JFrame jf = new JFrame("My Calculator");
static JPanel p1, p2, p3, p4, p5;
static CardLayout cl = new CardLayout();
static JButton b1 = new JButton("First");
static JButton b2 = new JButton("<<");
static JButton b3 = new JButton(">>");
static JButton b4 = new JButton("Last");
static String [] arr = {"Tanuj", "Mukarram", "Srinath", "Sumit", "Debnath"};
static JComboBox <String> jcb = new JComboBox<>(arr);
static JPanel p = new JPanel(cl);
static JLabel l1,l2,l3,l4,l5,l6,l7,l8,l9,l10;
static JTextField jt1,jt2,jt3,jt4,jt5;

public static void main(String [] rk)
{
p1 = new JPanel(); p1.setBackground(Color.RED);
p2 = new JPanel(); p2.setBackground(Color.CYAN);
p3 = new JPanel(); p3.setBackground(Color.MAGENTA);
p4 = new JPanel(); p4.setBackground(Color.YELLOW);
p5 = new JPanel(); p5.setBackground(Color.ORANGE);

jf.add(p);
p.add(p1, "Sumit");
p.add(p2, "Debnath");
p.add(p3, "Mukarram");
p.add(p4, "Srinath");
p.add(p5, "Tanuj");

JPanel buttons = new JPanel();
buttons.add(b1); buttons.add(b2); buttons.add(b3);
buttons.add(b4); buttons.add(jcb);

jf.add(buttons, BorderLayout.SOUTH);
CardListener l = new CardListener();
b1.addActionListener(l); b2.addActionListener(l);
b3.addActionListener(l); b4.addActionListener(l);
jcb.addActionListener(l);



ButtonGroup bg = new ButtonGroup();
JRadioButton r1 = new JRadioButton("Swim",true);     // it is default checkbox with selecting more than one option
JRadioButton r2 = new JRadioButton("Read"); //  here button group is used for mutual inclusion i.e. one option
JRadioButton r3 = new JRadioButton("Play");
JToggleButton jt = new JToggleButton("Okey");
bg.add(r1); bg.add(r2); bg.add(r3);
bg.add(jt); // can add any button like toogle, radio, checkbox in ButtonGroup
p4.add(r1); p4.add(r2); p4.add(r3); // as all implements the Abstract Method of ButtonGroup not normal Button
p4.add(jt);               // i.e. JButton, it don't have model state. In a buttongroup, only one could be selected

// JTable, should add in JScroll Pane, a scrollable panel


//p1.add(jts);
//p1.setLayout(null);
//jts.setBounds(50,50,700,100);

//JList similar to JTable but consis only single column.
    p2.setLayout(null);
  //  p1.setLayout(null);
    //    p1.add(l10);
      //      l10.setBounds(300,100,300,300);
    l1 = new JLabel("Name :");
    l2 = new JLabel("CGPA :");
    l3 = new JLabel("Qualification:");
    l4 = new JLabel("Field :");
    l5 = new JLabel("Contact No. :");
    l6 = new JLabel("My Resume ");
    l7 = new JLabel("Qualification :");
    l8  = new JLabel();
    l9 = new JLabel("Choose Image : ");
    JCheckBox c1 = new JCheckBox("Java");
    JCheckBox c2 = new JCheckBox("Python",true);
    JCheckBox c3 = new JCheckBox("C/C++");
       
        p2.add(l8);
            l8.setBounds(410,70,300,300);
        p2.add(l6);
            l6.setBounds(280,20,200,50);
            l6.setFont(new Font("Serif",3,30));
        p2.add(l1);
            l1.setBounds(50, 70,200,50);
            l1.setFont(new Font("Serif",3,17));
        p2.add(l2);
            l2.setBounds(50, 110,200,50);
            l2.setFont(new Font("Serif",3,17));
        p2.add(l3);
            l3.setBounds(50, 150,200,50);
            l3.setFont(new Font("Serif",3,17));
        p2.add(l4);
            l4.setBounds(50, 190,200,50);
            l4.setFont(new Font("Serif",3,17));
        p2.add(l5);
            l5.setBounds(50, 230,200,50);
            l5.setFont(new Font("Serif",3,17));
        p2.add(l7);
            l7.setBounds(50,270,200,50);
            l7.setFont(new Font("Serif",3,17));
        p2.add(c1);
            c1.setBounds(200,300,200,20);
        p2.add(c2);
            c2.setBounds(200,330,200,20);
        p2.add(c3);
            c3.setBounds(200,360,200,20);
        p2.add(l9);
            l9.setBounds(50,380,200,50);
            l9.setFont(new Font("Serif",3,17));
    JButton b = new JButton("Image");
    JButton sb = new JButton("Submit");
        b.setForeground(Color.RED);
        p2.add(b);
        b.setBounds(200,410,150,50);
        b.addActionListener(l);
        p2.add(sb);
        sb.setBounds(150,500,150,50);
        sb.addActionListener(l);
    jt1 = new JTextField();
    jt2 = new JTextField();
    jt3 = new JTextField();
    jt4 = new JTextField();
    jt5 = new JTextField();
    
        p2.add(jt1);
            jt1.setBounds(200,90,200,20);
            jt1.setFont(new Font("Serif",3,17));
        p2.add(jt2);
            jt2.setBounds(200,130,200,20);
            jt2.setFont(new Font("Serif",3,17));
        p2.add(jt3);
            jt3.setBounds(200,170,200,20);
            jt3.setFont(new Font("Serif",3,17));
        p2.add(jt4);
            jt4.setBounds(200,210,200,20);
            jt4.setFont(new Font("Serif",3,17));
        p2.add(jt5);
            jt5.setBounds(200,250,200,20);
            jt5.setFont(new Font("Serif",3,17));
        



jf.setSize(700, 700);
jf.setLocationRelativeTo(null);
jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//jf.setResizable(false);
jf.setIconImage(new ImageIcon("rabbit.jpg").getImage());
jf.getContentPane().setBackground(Color.CYAN);
jf.setVisible(true);
}
}
