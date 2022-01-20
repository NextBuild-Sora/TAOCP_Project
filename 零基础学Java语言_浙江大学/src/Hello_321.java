
/*
*	第3周 循环.
*	3.2 循环的例子.
*	3.2.1 计数循环.
*/

import java.util.Scanner;

public class Hello_321 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int count = 10;	//循环执行次数.
//		while (count >= 0)	//这条语句执行后会出现不一样的结果.
		while (count>0)
		{
			//	count = count-1;
			//System.out.println(count);	//先输出.
			System.out.println("发送" + count);
			count = count - 1;	//再减1.
		}
		System.out.println("最后一个(循环结束后的)：" + count);
		System.out.println("发射！");
	}

	
	
}
