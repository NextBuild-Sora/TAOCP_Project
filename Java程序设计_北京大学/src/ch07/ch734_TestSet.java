
/*

 * 第7章 工具类及常用算法
 • 7.3 集合
 	---ch734---
 	--Set 集--
 	• Set 集 两个重要的实现 HashSet及TreeSet.
	*其中TreeSet的底层是用TreeMap来实现的.
	• Set中对象不重复，即：
	*hashCode()不等.
	*如果hashCode()相等，再看equals或==是否为false.
	
*/


package ch07;

import java.util.*;
public class ch734_TestSet {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Set<String> set = new HashSet<String>();
		
		set.add("B");
		set.add("R");
		set.add("I");
		set.add("C");
		set.add("S A");
		
		System.out.println( set.contains("C") );
		
		for( String obj : set)
			System.out.println( obj );
		

	}

}

