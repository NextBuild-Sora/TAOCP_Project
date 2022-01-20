
/* 10.3 布局管理
 * 
 * ---ch1034---
 * -- 容器的嵌套使用举例 --
 * 
 */



package ch10;

import java.awt.*;
import javax.swing.*;

public class ch1034_NestedContainer extends JFrame {

	JLabel lbl = new JLabel( "Display Area(展示区)" );
	JPanel pnl = new JPanel();
	JButton b1 = new JButton("1");
	JButton b2 = new JButton("2");
	JButton b3 = new JButton("3");
	JButton b4 = new JButton("4");
	public ch1034_NestedContainer() {
		super("Nested Container（嵌套容器）");
		
		pnl.setLayout(new GridLayout(2, 2));
		pnl.add(b1);	pnl.add(b2);
		pnl.add(b3);	pnl.add(b4);
		
		add(lbl, BorderLayout.NORTH);
		add(pnl, BorderLayout.CENTER);
		
		setSize(250,140);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SwingUtilities.invokeLater( ()->{
			new ch1034_NestedContainer();
		} );
	}

}
