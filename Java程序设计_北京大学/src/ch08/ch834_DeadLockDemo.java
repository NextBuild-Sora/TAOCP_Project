
/* 
 * 第8讲 多线程
 *  线程的同步   
 * ---ch834---
 * --线程的死锁--
 * 
 */


package ch08;

class Worker
{
	int id;
	public Worker(int id) {this.id = id;}
	synchronized void doTaskWithCooperator(Worker other) {
		try { Thread.sleep(500); } catch(Exception e) {}
		synchronized (other) {
			System.out.println("doing" + id);
		}
	}
}

public class ch834_DeadLockDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Worker w1 = new Worker(1);
		Worker w2 = new Worker(2);
	Thread td1 = new Thread(()->{
		w1.doTaskWithCooperator(w2);
	});
	Thread td2 = new Thread(()->{
		w2.doTaskWithCooperator(w1);
	});
	td1.start();
	td2.start();

	}

}

