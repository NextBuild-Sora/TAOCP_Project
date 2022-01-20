

/*
 * 第10讲 图形用户界面
 * 
 * 10.2 实现图形用户界面的三步曲
 * 
 * • 设计和实现图形用户界面的工作主要有以下几点。
	• （1）创建组件（Component） 
		
	• （2）指定布局（Layout） 
		
	• （3）响应事件（Event） 
 *
 * ---ch1020----
	--• 示例 使用JFrame--
 * 
 * 
 */



package ch10;

import javax.swing.*;
import java.awt.*;

public class ch1020_TestJFrame extends JFrame 
{
	private JLabel lbl;
	
	public ch1020_TestJFrame()
	{
		super("Test JFrame()");
		
		lbl = new JLabel("Hello Swing");
		//add(lbl);
		getContentPane().add(lbl);
		
		setSize(400, 300);
		setDefaultCloseOperation(EXIT_ON_CLOSE); 	//设置为可关闭
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new ch1020_TestJFrame().setVisible(true);

	}

}


