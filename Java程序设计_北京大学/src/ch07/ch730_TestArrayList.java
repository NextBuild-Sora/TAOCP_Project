
/*
 * 第7章 工具类及常用算法
 • 7.3 集合
 	---ch730---
 	--列表--
 	• List接口： 线性表（linear list） 
 		*主要的实现类是 ArrayList. LinkedList， 以及早期的Vector。

*/


package ch07;

import java.util.*;

public class ch730_TestArrayList {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList h = new ArrayList();
		h.add("lst");
		h.add("2nd");
		h.add(new Integer(3));
		h.add(new Double(4.0));
		h.add("2nd"); 	//重复元素，加入。
		h.add(new Integer(3)); 	//重复元素，加入。
		m1(h);
		
	}
	public static void m1(List s) {
		System.out.println(s);
	}

}

//本应用程序输出结果如下[1st, 2nd, 3, 4.0, 2nd, 3]


