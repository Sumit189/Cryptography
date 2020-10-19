import java.time.*;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.Set;
import java.awt.event.*;
import javax.swing.event.*;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;

class listen implements ActionListener {

    @Override
    public void actionPerformed(ActionEvent e) {
        // TODO Auto-generated method stub
        if (e.getSource() == zoneclock.cb) {
            String type = (String) zoneclock.cb.getItemAt(zoneclock.cb.getSelectedIndex());
            zoneclock.zone.forEach(x-> {
                if (x.contains(type)) {
                    ZoneId z1 = ZoneId.of(x);
                    LocalTime t2 = LocalTime.now(z1);
                    zoneclock.jf.add(zoneclock.out);
                    zoneclock.out.setText(t2.toString());
                    zoneclock.out.setBounds(150, 80, 300, 40);
                }
            });
        }
    }

}

public class zoneclock {
    static JFrame jf;
    static JComboBox cb;
    static JLabel ind, indt;
    static JLabel out;
    static Set<String> zone = ZoneId.getAvailableZoneIds();

    public static void main(String[] args) {
        jf = new JFrame("ZOne");
        jf.setLayout(null);
        ind = new JLabel("india");
        indt = new JLabel();
        out = new JLabel();
        LocalTime t1 = LocalTime.now();
        indt.setText(t1.toString());
        String[] coun = { "Berlin", "Brazil" };
        cb = new JComboBox<>(coun);

        jf.add(ind);
        ind.setBounds(20, 30, 100, 40);
        jf.add(indt);
        indt.setBounds(20, 100, 300, 40);
        jf.add(cb);
        cb.setBounds(150, 40, 100, 40);

        listen ls = new listen();
        cb.addActionListener(ls);

        jf.setSize(300, 300);
        jf.setLocationRelativeTo(null);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setVisible(true);
    }
}
