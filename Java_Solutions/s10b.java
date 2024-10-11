package Java_Solutions;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class s10b {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Compound Interest Calculator");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        JLabel principalLabel = new JLabel("Principal Amount:");
        principalLabel.setBounds(20, 20, 150, 30);
        frame.add(principalLabel);

        JTextField principalField = new JTextField();
        principalField.setBounds(200, 20, 150, 30);
        frame.add(principalField);

        JLabel rateLabel = new JLabel("Interest Rate (%):");
        rateLabel.setBounds(20, 60, 150, 30);
        frame.add(rateLabel);

        JTextField rateField = new JTextField();
        rateField.setBounds(200, 60, 150, 30);
        frame.add(rateField);

        JLabel timeLabel = new JLabel("Time (Yrs):");
        timeLabel.setBounds(20, 100, 150, 30);
        frame.add(timeLabel);

        JTextField timeField = new JTextField();
        timeField.setBounds(200, 100, 150, 30);
        frame.add(timeField);

        JLabel totalLabel = new JLabel("Total Amount:");
        totalLabel.setBounds(20, 140, 150, 30);
        frame.add(totalLabel);

        JTextField totalField = new JTextField();
        totalField.setBounds(200, 140, 150, 30);
        totalField.setEditable(false);
        frame.add(totalField);

        JLabel interestLabel = new JLabel("Interest Amount:");
        interestLabel.setBounds(20, 180, 150, 30);
        frame.add(interestLabel);

        JTextField interestField = new JTextField();
        interestField.setBounds(200, 180, 150, 30);
        interestField.setEditable(false);
        frame.add(interestField);

        JButton calculateButton = new JButton("Calculate");
        calculateButton.setBounds(50, 220, 100, 30);
        frame.add(calculateButton);

        JButton clearButton = new JButton("Clear");
        clearButton.setBounds(160, 220, 100, 30);
        frame.add(clearButton);

        JButton closeButton = new JButton("Close");
        closeButton.setBounds(270, 220, 100, 30);
        frame.add(closeButton);

        calculateButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                double principal = Double.parseDouble(principalField.getText());
                double rate = Double.parseDouble(rateField.getText()) / 100;
                double time = Double.parseDouble(timeField.getText());

                double amount = principal * Math.pow(1 + rate, time);
                double interest = amount - principal;

                totalField.setText(String.format("%.2f", amount));
                interestField.setText(String.format("%.2f", interest));
            }
        });

        clearButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                principalField.setText("");
                rateField.setText("");
                timeField.setText("");
                totalField.setText("");
                interestField.setText("");
            }
        });

        closeButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });

        frame.setVisible(true);
    }
}
