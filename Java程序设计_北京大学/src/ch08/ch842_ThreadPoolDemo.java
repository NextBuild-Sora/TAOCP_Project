
/* 第8讲 
 * 8.4 并发API
 * 
 * ---ch842---
 * --使用线程池--
	• 线程池相关的类
	*ExecutorService 接口、ThreadPoolExecutor 类 
	  *Executors 工具类
	• 常见的用法
	*ExecutorService pool = Executors.newCachedThreadPool();
	*使用其execute( Runnable r)方法
*/


package ch08;

import java.util.concurrent.*;

public class ch842_ThreadPoolDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ExecutorService pool = Executors.newCachedThreadPool();
		MyTask t1 = new MyTask(5);
		MyTask t2 = new MyTask(7);
		MyTask t3 = new MyTask(8);
		pool.execute(t1);
		pool.execute(t2);
		pool.execute(t3);
		pool.shutdown(); //关闭
		
	}

}

class MyTask implements Runnable
{
	int n=10;
	public MyTask(int n) {this.n = n;}
	public void run() {
		for(int i=0; i<n; i++)System.out.print(i);
	}
}

