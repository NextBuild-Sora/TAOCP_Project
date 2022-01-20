
/*
 第8章 多线程
 • 8.1 线程的创建
 	
 	---ch811---
 	
 	创建线程的两种方法:
// 	• 1．通过继承Thread类创建线程.
 	• 2．通过向Thread()构造方法传递Runnable对象来创建线程.

*/

package ch08;

public class ch811_TestThread2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MyTask mytask = new MyTask(10);
		Thread thread = new Thread(mytask);
		thread.start();

	}

}

//这是第2种方法。
class MyTask implements Runnable{
	private int n;
	public MyTask( int n ) {
		this.n = n;
	}
	
	//线程体---- run()方法来实现的。如一个循环.
	public void run() {
		for(int i=0; i<n; i++) {
			System.out.println(" " + i);
			try {
				Thread.sleep(500);
			}catch( InterruptedException e) {}
		}
	}
}

