

/*
 * 第7章 工具类及常用算法
 • 7.3 集合
 	---ch732---
 	--Queue 队列--
	--队列Queue--
	• 队列(Queue)，也是重要的线性数据结构。
	*队列遵循“先进先出”(First In First Out，FIFO)的原则。
	*固定在一端输入数据(称为入队)，另一端输出数据(称为出队)。
	
*/



package ch07;

import java.util.*;

public class ch733_TestQueue {
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Queue<Integer> q = new LinkedList<>();
		
		for(int i=0; i<5; i++)
			q.offer( i ); 	//提出
		
		
		while( !q.isEmpty() )
			System.out.println( q.poll() ); 	//输出打印 投票

	}

}


