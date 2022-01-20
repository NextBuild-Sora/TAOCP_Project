
/*
 第8章 多线程
 • 8.1 线程的创建
 
 ---ch812---
 
 	匿名类及Lambda表达式

*/

package ch08;

public class ch812_TestThread4Anonymous {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//匿名类实现Runnable: 
		new Thread() {
			public void run() {
				for(int i=0; i<10; i++)
					System.out.println(i);
			}
		}.start();
		
		//Lambda表达式:
		new Thread( () -> {
//			System.out.println();
			
			for(int i=0; i<10; i++)
				System.out.println(" " + i);
		} ).start();

	}

}
