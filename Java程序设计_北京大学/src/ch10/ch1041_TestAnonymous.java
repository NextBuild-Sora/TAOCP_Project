

/* 10.4 事件处理
 * ---ch1041---
 * -- 实现Listener的方法 --
 * 
	使用匿名类的例子
	• 其中用匿名类实现了MouseMotionListener及继承了WindowAdapter，
		同时实例化了这个匿名 类的对象。

 */



package ch10;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ch1041_TestAnonymous extends JFrame {

	JTextField text = new JTextField(30);
	
	public ch1041_TestAnonymous() {
		super("Test listener whith anonymous class（使用匿名类测试侦听器）");
		add(new JLabel("Please movev moue（请移动鼠标）"), BorderLayout.NORTH);
		add(text, BorderLayout.SOUTH);
		
		getContentPane().addMouseMotionListener(new MouseMotionListener() {
			public void mouseDragged(MouseEvent e) {}
			public void mouseMoved(MouseEvent e) {
				String s = "mouse position（鼠标位置） (" + e.getX() + ", " + e.getY() + ")";
				text.setText(s);
			}
		});
		addWindowListener( new WindowAdapter() {
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});
		setSize(400, 300);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SwingUtilities.invokeLater(()->{
			new ch1041_TestAnonymous();
		});

	}

}



