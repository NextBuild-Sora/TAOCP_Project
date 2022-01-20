

/*
 * 10.4 事件处理
 * 
 * --- ch1044 ---
 * 	-- 应用示例• 小小计算器 --
		
*/



package ch10;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ch1044_JCalculator extends JFrame implements ActionListener {
	
	private final String[] str = {
			"7", "8", "9", "/", 
			"4", "5", "6", "*",
			"1", "2", "3", "-", 
			".", "0", "=", "+"	
	};
	
	JButton[] buttons = new JButton[str.length];
	JButton reset = new JButton("CE（清除）");
	JTextField display = new JTextField("0");
	
	public ch1044_JCalculator() {
		super("Calculator（计算器）");
			Font font = new Font("Consonlas", Font.BOLD, 18);
		

			//	add components
			JPanel pnlHead = new JPanel(new BorderLayout());
		pnlHead.add( display, BorderLayout.CENTER);
		pnlHead.add( reset, BorderLayout.EAST );
			display.setFont(font);
			reset.setFont(font);
			
		JPanel pnlBody = new JPanel(new GridLayout(4, 4));
		for(int i=0; i<str.length; i++) {
			buttons[i] = new JButton(str[i]);
				buttons[i].setFont(font);
			pnlBody.add(buttons[i]);
		}
		
		getContentPane().setLayout(new BorderLayout());
		getContentPane().add(BorderLayout.NORTH, pnlHead);
		getContentPane().add(BorderLayout.CENTER, pnlBody);
		
		//  register listeners
		for(int i=0; i<str.length; i++)
			buttons[i].addActionListener(this);
		reset.addActionListener(this);
		display.addActionListener(this);
		

			// set frame properties
			setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		setSize(400, 380);
		setVisible(true);
		
	}
	
	public void actionPerformed(ActionEvent e) {
		Object source = e.getSource();
		String cmd = e.getActionCommand();
		if(source == reset)
			handleReset();
		else if("0123456789.".indexOf(cmd) >= 0)
			handleNumber(cmd);
		else 
			handleOperator(cmd);
			
	}
	
	boolean isFirstDigit = true;
	double number = 0.0;
	String operator = "=";
	
	public void handleNumber(String key) {
		if(isFirstDigit)
			display.setText(key);
		else if(!key.equals("."))
			display.setText(display.getText() + key);
		else if(display.getText().indexOf(".") < 0)
			display.setText(display.getText() + ".");
		isFirstDigit = false;
	}
	
	public void handleReset() {
		display.setText("0");
		isFirstDigit = true;
		operator = "=";
	}
	
	public void handleOperator(String cmd) {
		double dDisplay = Double.valueOf(display.getText());
		switch(operator) {
		case "+": number += dDisplay; break; 
		case "-": number -= dDisplay; break; 
		case "*": number *= dDisplay; break; 
		case "/": number /= dDisplay; break; 
		case "=": number = dDisplay; break; 
		}
		display.setText(String.valueOf(number));
	operator = cmd;
	isFirstDigit = true;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SwingUtilities.invokeLater( ()->{
			new ch1044_JCalculator();
		} );

	}

}




