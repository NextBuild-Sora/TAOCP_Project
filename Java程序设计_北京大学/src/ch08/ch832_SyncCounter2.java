
/*
 * 第8将 多线程
 * 8.3 线程的同步
 * 	---ch832---
 *  --同步--
*关键字synchronized 用来与对象的互斥锁联系。

 --synchronized--
• synchronized的用法
*对代码片断：
	• synchronized(对象){ 。。。。} 
*对某个方法：
	• synchronized 放在方法声明中，
	• public synchronized void push(char c ){ 。。。。} 
	• 相当于对synchronized(this), 表示整个方法为同步方法。

*/


package ch08;

public class ch832_SyncCounter2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Num num = new Num();
		Thread counter1 = new Counter(num);
		Thread counter2 = new Counter(num);
		for(int i=0; i<10; i++) {
			num.testEquals();
			try {
				Thread.sleep(100);
			}catch(InterruptedException e) {}
		}

	}

}

class Num
{
	private int x=0;
	private int y=0;
	synchronized void increase() {
		x++;
		y++;
	}
	synchronized boolean testEquals() {
		boolean ok = (x==y);
		System.out.println(x + ", " + y + ": " + ok);
		return ok;
	}
}

class Counter extends Thread
{
	private Num num;
	Counter( Num num ){
		this.num = num;
		this.setDaemon(true);
		this.setPriority(MAX_PRIORITY);
		this.start();
	}
	public void run() {
		while(true) {
			num.increase();
		}
	}
}