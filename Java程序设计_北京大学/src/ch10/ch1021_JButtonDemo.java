

/*
 * 第10讲 图形用户界面
 * 
 * 10.2 实现图形用户界面的三步曲
 *  
 * • 设计和实现图形用户界面的工作主要有以下几点。
	• （1）创建组件（Component） 
	• （2）指定布局（Layout） 
	• （3）响应事件（Event）
	 
 * ---ch1021----	
	-- • 示例 使用按钮--
 * 
 * 
 */



package ch10;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.*;

public class ch1021_JButtonDemo extends JFrame {
	JButton b1 = new JButton("JButton 1");
	JButton b2 = new JButton("JButton 2");
	JTextField t = new JTextField(20);
	public ch1021_JButtonDemo() {
		b1.setToolTipText("Press Butto will show msg");
		b1.setIcon(new ImageIcon("cupHJbutton.gif"));
		
		getContentPane().setLayout(new FlowLayout());
		getContentPane().add(b1);
		getContentPane().add(b2);
		getContentPane().add(t);
		
		setSize(500, 400);
		setDefaultCloseOperation(DISPOSE_ON_CLOSE);
		ActionListener al = new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String name = 
						((JButton)e.getSource()).getText();
				t.setText(name + "Pressed");
			}
		};
		b1.addActionListener(al);
		b2.addActionListener(al);
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new ch1021_JButtonDemo().setVisible(true);
		

	}

}



