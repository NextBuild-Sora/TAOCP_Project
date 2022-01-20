

/*
 * 10.3 布局管理
 * 
 * ---ch1032---
 * -- GridLayout 布局管理器 --
 * 
 */


package ch10;

import java.awt.*;
import javax.swing.*;

public class ch1032_TestGridLayout extends JFrame {
	JButton[] buttons = new JButton[20];
	public ch1032_TestGridLayout() {
		for( int i=0; i<buttons.length; i++ )
			buttons[i] = new JButton( ""+(i+1) );
		
		setLayout(new GridLayout(4, 5));
		
		for( int i=0; i<buttons.length; i++ )
			add( buttons[i] );
		
		setSize(400, 400);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SwingUtilities.invokeLater( ()->{
			new ch1032_TestGridLayout();
		} );

	}

}


