

/*
 * 10.4 事件处理
 * --- ch1043 ---
 * 	-- 事件与线程 --
		• 线程中，如果要更新界面，要放到the event dispatching thread.
		• 也就是要调用 SwingUtilities.invokeLater()方法.
 * */


package ch10;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class MyFrame extends JFrame{
	JButton btn = new JButton("Start(开始)");
	JLabel lbl = new JLabel("");
	public MyFrame() {
		this.setTitle("Test InvokeLater（测试 调用随后）");
		this.setSize(400, 300);
		lbl.setFont(new Font("Times New Rome（时代新罗马）", 0, 48));
		lbl.setHorizontalAlignment( SwingConstants.CENTER );
		getContentPane().setLayout(new BorderLayout());
		getContentPane().add(btn, BorderLayout.NORTH);
		getContentPane().add(lbl, BorderLayout.CENTER);
		btn.addActionListener( e->{
			new Thread( ()->{
				for(int i=10; i>=0; i--) {
					final int j = i;
					SwingUtilities.invokeLater(()->{
						lbl.setText(""+j);
					});
					try { Thread.sleep(200); }
					catch(Exception ex) {}
				}
			} ).start();
		} );
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
}

public class ch1043_InvokeLaterDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SwingUtilities.invokeLater( ()->{
			new MyFrame().setVisible(true);
		} );

	}

}



