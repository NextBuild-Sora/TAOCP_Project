
/*
 第8章 多线程
 • 8.1 线程的创建
 
 ---ch814---
 
 	-多线程-
  	 -多线程绘图-

*/


package ch08;

import java.awt.*;
import java.applet.*;
import java.awt.event.*;
import javax.swing.*;
	
public class ThreadDrawJ extends JFrame {
	
	MovingShape_1 [] shapes;
	
	public void init() {
		setLayout(null);
		setSize(426,266);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);

		shapes = new MovingShape_1[ 10 ];
		for( int i=0; i<shapes.length; i++ ){
		    shapes[i] = new MovingShape_1(this);
			shapes[i].start();
		}
	}
	
	public static void main(String[] args) //加入main,使之能当Application应用
	{
		// TODO Auto-generated method stub
//		ch814_ThreadDrawJ f = new ch814_ThreadDrawJ();		
		ThreadDrawJ f = new ThreadDrawJ();
		f.init();
		
	}

}

class MovingShape_1 extends Thread
{
	private int size=100;
	private int speed = 10;
	private Color color;
	private int type;
	private int x,y,w,h,dx,dy;
	protected java.awt.Component app;
		
		public boolean stopped;
		
	MovingShape_1(JFrame app){
		this.app = app;
		x = (int)(Math.random() * app.getSize().width);
		y = (int)(Math.random() * app.getSize().height);
		w = (int)(Math.random() * size);
		h = (int)(Math.random()* size);
		dx = (int)(Math.random() * speed );
		dy = (int)(Math.random() * speed );
		color = new Color(
				(int)(Math.random()*128+128),
				(int)(Math.random()*128+128),
				(int)(Math.random()*128+128));
		
		type = (int)(Math.random() * 3);
	}
	
	public void run()
    {
        while( true ){
			if( stopped ) break;
			
			//draw(); 
			//• 在线程中更新图形化界面
			SwingUtilities.invokeLater( ()->{
				draw(); 
			});

            try{ Thread.sleep(130); } catch( InterruptedException e ){}
        }
    }

	void draw(){
		x += dx;
		y += dy;
		if( x<0 || x+w>app.getSize().width ) dx = -dx;
		if( y<0 || y+h>app.getSize().height) dy = -dy;
		
		Graphics g = app.getGraphics();
		switch( type ){
			case 0:
				g.setColor(color);
				g.fillRect( x,y,w,h ); 
				g.setColor( Color.black );
				g.drawRect( x,y,w,h );
				break;
			case 1: 
				g.setColor(color);
				g.fillOval( x,y,w,h ); 
				g.setColor( Color.black );
				g.drawOval( x,y,w,h );
				break;
			case 2: 
				g.setColor(color);
				g.fillRoundRect( x,y,w,h,w/5,h/5); 
				g.setColor( Color.black );
				g.drawRoundRect( x,y,w,h,w/5,h/5 );
				break;
		}
	}
}

