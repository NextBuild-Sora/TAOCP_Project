

/*
 * 10.4 事件处理
 * ---ch1040---
 * -- 事件 简单示例 --
 * 
	• 事件及事件监听器
		*事件（Event） 
			• 鼠标、键盘、布局改变等等操作等
		*事件监听器（Event Listener)
 			• 对这些事件作出响应的程序
 	
 */


package ch10;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ch1040_TestActionEvent {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		JFrame f = new JFrame("Test（）");
		JButton btn = new JButton("Press Me（）! ");
		f.add(btn);
		
		ActionListener al = new MyListener();
		btn.addActionListener(al);
		
		f.setSize(300, 120);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setVisible(true);

	}

}

class MyListener implements ActionListener{
	@Override
	public void actionPerformed(ActionEvent e) {
		System.out.println("a button has been pressed（一个按钮被按下）");
	}
	
}

