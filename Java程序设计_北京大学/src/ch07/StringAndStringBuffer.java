

/*
 * 
 第7章 工具类及常用算法
 • 7.2 字符串和日期
 	---ch720---
 	--字符串--
 	• 字符串可以分为两大类.
	*String类: 
		• 创建之后不会再做修改和变动，即 immutable.
	*StringBuffer、StringBuilder类:  
		• 创建之后允许再做更改和变化.
		• 其中 StringBuilder是JDK1.5增加的，它是非线程安全的.
	• 特别注意
	*在循环中使用String的+=可能会带来效率问题.
  */


package ch07;

import java.util.*;

public class StringAndStringBuffer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String a = "a";
		String s = "";
		StringBuffer sb = new StringBuffer();
		
		final int N = 10000;
		
		long t0 = System.currentTimeMillis();
		for( int i=0; i<N; i++ ) s+=a;
		long t1 = System.currentTimeMillis();
		for(  int i=0; i<N; i++ ) sb.append(s);
		long t2 = System.currentTimeMillis();
		
		System.out.println( t1-t0);
		System.out.println( t2-t1);

	}

}


