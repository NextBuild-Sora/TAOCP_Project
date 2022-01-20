

/*
 * 
 * 10.6 Applet
 * ---ch1060---
 * -- Applet程序 --
 * 
 */


package ch10;

import java.awt.*;
import java.applet.*;
import javax.swing.*;

public class ch1060_HelloWorldApplet extends JApplet {

//	public static void main(String[] args) {
		// TODO Auto-generated method stub

//	}
	
	public void paint(Graphics g) {
		g.drawString("Hello world!", 20,20 );
		}

}


