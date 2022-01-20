import java.util.Scanner;

/* 第7周 函数
 * 7.1 函数定义与调用
 * 7.1.1_1 函数定义
 * 素数求和
 */

public class Hello_711_1 {
	public static void sum(int a, int b)
	{
		int i;
		int sum;
		sum = 0;
		for ( i=a; i<=b; i++ )
		{
			sum += i;
		}
		System.out.println(a+"到"+b+"的和是"+sum);
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
//		int i;
//		int sum;
		sum(1,10);
		sum(20,10);
		sum(35,45);
		
//		sum = 0;
//		for ( i=1; i<=10; i++ )
//		{
//			sum += i;
//		}
//		System.out.println(1+"到"+10+"的和是"+sum);
//		
//		sum = 0;
//		for ( i=20; i<=30; i++ )
//		{
//			sum += i;
//		}
//		System.out.println(20+"到"+30+"的和是"+sum);
//		
//		sum = 0;
//		for ( i=35; i<=50; i++ )
//		{
//			sum += i;
//		}
//		System.out.println(35+"到"+50+"的和是"+sum);
//		

	}

}
