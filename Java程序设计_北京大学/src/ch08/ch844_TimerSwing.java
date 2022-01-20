
/*
 * ---ch844---
 * --使用Timer--
 * 
 * • 使用 javax.swing.Timer 类 
  		*重复执行ActionListener
 */

package ch08;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.Timer;

public class ch844_TimerSwing extends JFrame
{
	
	Timer timer;
	public void init() 
	{
		setLayout(null);
		setSize(400, 100);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
		
		timer = new Timer(1000, (e)->{
			setTitle( new java.util.Date().toString());
		});
		timer.start();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new ch844_TimerSwing().init();

	}

}
