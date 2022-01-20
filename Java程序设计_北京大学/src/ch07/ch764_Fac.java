

/*
 * 第7章 工具类及常用算法
 * 7.6 常用算法
 *  ---ch764--
 *  递归
	• 递归(recursive)就是一个过程调用过程本身。
	*在递归调用中，一个过程执行的某一步要用到它的上一步(或上几步)的结果.
	
	• 示例
	Fac.java 用递归方法求阶乘.
	
	• 递归算法的基本模式:f(n){ f(n-1); }
	
 */

package ch07;

public class ch764_Fac {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println( "Fac of 5 is: " + fac(5) );

	}
	static long fac( int n ) {
		if( n==0 ) return 1;
		else return fac(n-1) * n;
	}

}
