

/*
 * 10.3 布局管理
 * 
 * ---ch1030---
 * -- FlowLayout布局管理器 --
 * 
 */
		

package ch10;

import java.awt.*;
import javax.swing.*;

public class ch1030_TestFlowLayout extends JFrame {

	JButton[] buttons = new JButton[8];
	public ch1030_TestFlowLayout() {
		for( int i=0; i<buttons.length; i++)
			buttons[i] = new JButton("Button（纽扣）" + (i+1) );
		
		setLayout( new FlowLayout(FlowLayout.LEFT, 10, 5) );
		
		for( int i=0; i<buttons.length; i++ )
			add( buttons[i] );
		
		setSize(400, 300);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SwingUtilities.invokeLater( ()->{
			new ch1030_TestFlowLayout();
		} );

	}

}


