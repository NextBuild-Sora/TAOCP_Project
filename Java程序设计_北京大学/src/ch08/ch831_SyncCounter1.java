

/*
 * 第8将 多线程
 * 8.3 线程的同步
 * 	---ch831---
 * 	 --多线程同步--
 * 
 */


package ch08;

public class ch831_SyncCounter1 
{
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Num_0 num = new Num_0();
		Thread  counter1 = new Counter_0(num);
		Thread counter2 = new Counter_0(num);
		for(int i=0; i<10; i++) {
			if(!num.testEquals()) break;
			try {
				Thread.sleep(100);
			}catch(InterruptedExcption e) {}
		}
		
	}

}

class Num_0
{
	private int x=0;
	private int y=0;
	void increase() {
		x++;
		y++;
	}
	boolean testEquals() {
		boolean ok = (x==y);
		System.out.println(x + "," + y + ": " + ok);
		return ok;
	}
}

class Counter_0 extends Thread
{
	private Num_0 num;
	Counter_0(Nun_0 num){
		this.num = num;
		this.setDaemon(true);
		this.setPriority(MIN_PRIORITY);
		this.start();
	}
	public void run() {
		while(true) {
			num.increase();
		}
	}
}

