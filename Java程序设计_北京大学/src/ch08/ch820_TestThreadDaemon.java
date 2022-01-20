
/*
 第8章 多线程
 • 8.2 线程的控制
 
 	---ch820---

 	--后台线程--
 	
 • 线程有两种
*一类是普通线程（非Daemon线程）.

*一类是Daemon线程（守护线程，后台线程）.

 • 使用setDaemon(true);
 * 
 */


package ch08;

import java.util.*;

public class ch820_TestThreadDaemon {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread t = new MyThread_0();
		t.setDaemon(true);
		t.start();
		
		System.out.println("Main（主函数）-- " + new Date());
		try { Thread.sleep(500); }
		catch(InterruptedException ex) {}
		System.out.println("Main End（主函数结束）");

	}

}

class MyThread_0 extends Thread{
	public void run() {
		for(int i=0; i<10; i++) {
			System.out.println( i + "--" + new Date());
			try { Thread.sleep(100); }
			catch( InterruptedException ex ) {}
		}
	}
}

