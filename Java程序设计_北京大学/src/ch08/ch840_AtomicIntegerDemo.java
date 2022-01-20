
/*
 * 第8讲
 * 8.4 并发API
 * 
 * ---ch840---
 * 
 * --原子变量--
	• java.util.concurrent.atomic 包 
		*AtomicInteger 类 
		*getAndIncrement（）方法

*/


package ch08;

import java.util.concurrent.atomic.AtomicInteger;
public class ch840_AtomicIntegerDemo {
	
	static int n = 0;
	static AtomicInteger cnt = new AtomicInteger(0);

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		final int NUM=1000;
		Thread [] threads = new Thread[NUM];
		for(int i=0; i<NUM; i++) {
			threads[i] = new Thread() {
				public void run() {
					n++;
					cnt.getAndIncrement();
				}
			};
		}
		for(int i=0; i<NUM;i++) threads[i].start();
		try { Thread.sleep(3000); }
		catch(InterruptedException ex) {}
		System.out.printf("%d %b\n", n, n==NUM);
		System.out.printf("%d %b\n",cnt.get(), cnt.get()==NUM);
		
	}

}



