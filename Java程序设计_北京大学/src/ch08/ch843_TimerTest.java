
/*
 * ---ch843---
 * 使用Timer
	• 使用 java.util.Timer 类
		*重复某件事
 */

package ch08;

import java.util.*;

public class ch843_TimerTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Timer timer = new Timer("display");
		TimerTask task = new MyT();
		timer.schedule(task, 1000, 1000);

	}

}

class MyT extends TimerTask{
	int n = 0;
	public void run() {
		n++;
		System.out.println(new Date());
		System.out.println("---" + n);
		
	}
}
