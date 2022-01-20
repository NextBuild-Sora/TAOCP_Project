

/*
 * 第7章 工具类及常用算法
 • 7.3 集合
 	---ch732---
 	--Stack 栈--
	• 是遵循“后进先出”(Last In First Out, LIFO)原则
	• 重要线性数据结构
	• 包含三个方法
	public Object push(Object item)：将指定对象压入栈中。
	Public Object pop()：将 栈最上面的元素从栈中取出，并返回这个对象。
	public boolean empty()：判断栈中没有对象元素。
	
*/



package ch07;

import java.util.*;

public class ch732_TestStack {
	
	static String[] months = {
			"January-1", "February-2", "March-3", "April-4",
			"May-5", "June-6", "July-7", "August-8", "September-9",
			"October-10", "November-11", "December-12" 
	};

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack<String> stk = new Stack<>();
		
		for(int i=0; i<months.length; i++)
			stk.push(months[i]+"");
		
		System.out.println("stk= " + stk);
		
		System.out.println("popping elements（元素出栈）: ");
		
		while(!stk.empty())
			System.out.println(stk.pop());

	}

}


