
/*
 * 第7章 工具类及常用算法
 * 7.6 常用算法
 * 	---ch761---
 * 	遍试
		• 遍试（穷举，exhaust algorithm）. 
		• 在有限的范围内，可以对所有的值都进行试验和判断，从而找到满足条件的值.
	--求9999以内的完全数--
	
	• 遍试算法基本的模式：for(;;){ if(); }
	
 */



package ch07;



public class ch761_All_628 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(int n=1; n<=9999; n++)
			if( n==divsum(n) ) System.out.println(n);
	}
	
	public static int divsum( int n ) {
		int s = 0;
		for(int i=1; i<n; i++) 
			if(n%i == 0) s+=i;
		return s;
		
	}
	

}


