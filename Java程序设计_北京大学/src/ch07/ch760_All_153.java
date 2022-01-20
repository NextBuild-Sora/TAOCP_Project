
/*
 * 第7章 工具类及常用算法
 * 7.6 常用算法
 * 	---ch760---
 * 	遍试
		• 遍试（穷举，exhaust algorithm）. 
		• 在有限的范围内，可以对所有的值都进行试验和判断，从而找到满足条件的值.
	--求三位的水仙花数--
	
	• 遍试算法基本的模式：for(;;){ if(); }
	
 */



package ch07;



public class ch760_All_153 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(int a=0; a<=9; a++)
			for(int b=0; b<=9; b++)
				for(int c=0; c<+9;c++)
					if( a*a*a+b*b*b+c*c*c== 100*a+10*b+c )
						System.out.println( 100*a+10*b+c );

	}

}
