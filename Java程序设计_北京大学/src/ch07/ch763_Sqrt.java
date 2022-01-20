

/*
 * 第7章 工具类及常用算法
 * 7.6 常用算法
 * 	---ch763---
 * 	迭代
	• 迭代（iterative algorithm） 
	• 是多次利用同一公式进行计算，每次将计算的结果再代入公式进行计算，从而逐步逼近精确解.

		--Sqrt.java 自编一个函数求平方根--
	
	• 迭代的基本模式:while() { x = f(x); }
	
 */



package ch07;



public class ch763_Sqrt {

	public static void main(String[] args) {
		System.out.println( sqrt(98.0));
		System.out.println( Math.sqrt(98.0));

	}
	
	static double sqrt( double a ) {
		double x=1.0;
		do {
			x = (x+a/x)/2;
			System.out.println(x+", " + a/x);
		}while( Math.abs(x*x-a) /a > 1e-6);
		return x;
	}
	

}


