
/*
 第8章 多线程
 • 8.1 线程的创建
 	
 	---ch810---
 	
 	创建线程的两种方法:
 	• 1．通过继承Thread类创建线程.
// 	• 2．通过向Thread()构造方法传递Runnable对象来创建线程.

*/

package ch08;

public class ch810_TestThread1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread t = new MyThread(100);
		t.start();

	}

}

//这是第一种方法。
class MyThread extends Thread{
	private int n;
	public MyThread( int n ) {
		super();
		this.n = n;
	}
	
	//线程体---- run()方法来实现的。如一个循环.
	public void run() {
		for(int i=0; i<n; i++) {
			System.out.println(" " + i);
		}
	}
}
