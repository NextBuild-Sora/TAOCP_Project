
/*
 * 10.3 布局管理
 * 
 * ---ch1031---
 * -- BorderLayout 布局管理器 --
 * 
 */


package ch10;

import java.awt.*;
import javax.swing.*;

public class ch1031_TestBorderLayout extends JFrame {

	public ch1031_TestBorderLayout() {
		setLayout(new BorderLayout());
		
		add(new Button("North（北）"), BorderLayout.NORTH);
		add(new Button("South（南）"), BorderLayout.SOUTH);
		add(new Button("East（东）"), BorderLayout.EAST);
		add(new Button("West（西）"), BorderLayout.WEST);
		add(new Button("Center（中）"), BorderLayout.CENTER);
		
		setSize(400, 300);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SwingUtilities.invokeLater( ()->{
			new ch1031_TestBorderLayout();
		} );

	}

}



