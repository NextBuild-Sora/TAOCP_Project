
/*
 * 第8讲
 * 8.4 并发API
 * 
 * ---ch841---
 * 
 * --并发的集合类--
	• java.util.concurrent包中增加了一些方便的类。
		
*/


package ch08;

import java.util.concurrent.*;

class Producer_0 implements Runnable
{
	private BlockingQueue<Integer> queue;
	public Producer_0(BlockingQueue<Integer> queue) {
		this.queue = queue;
	}
	public void run() {
		for(int i=0; i<=10; i++) {
			try {
				Thread.sleep( (int)(Math.random()*10) );
				queue.put(i);
				System.out.println("Produce " + i + ".");
			}catch(InterruptedException ex) {}
		}
	}
}

class Consumer_0 implements Runnable
{
	private BlockingQueue<Integer> queue;
	public Consumer_0(BlockingQueue<Integer> queue) {
		this.queue = queue;
	}
	public void run() {
		for(int i=0; i<=100; i++) {
			try {
				Thread.sleep((int)(Math.random()*20));
				Integer product = queue.take();
				System.out.println("Consume" + product + ".");
			}catch(InterruptedException ex) {}
		}
	}
}

public class ch841_BlockingQueueDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(3);
		new Thread(new Producer_0(queue)).start();
		new Thread(new Consumer_0(queue)).start();

	}

}
