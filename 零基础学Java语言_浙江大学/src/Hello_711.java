import java.util.Scanner;

/* 第7周 函数
 * 7.1 函数定义与调用
 * 7.1.1 函数定义
 */

public class Hello_711 {
	public static boolean isPrime(int i)
	{
//		素数
		boolean isPrime = true;
		for ( int k=2; k<i; k++ )
		{
			if ( i % k == 0 )
			{
				isPrime = false;
				break;
			}
		}
		return isPrime;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int m = in.nextInt();
		int n = in.nextInt();
		if ( m==1 ) m=2;
		int cnt = 0;
		int sum = 0;
		for ( int i=m; i<n; i++ )
		{
//			boolean isPrime = true;
//			for ( int k=2; k<i; k++ )
//			{
//				if ( i % k == 0 )
//				{
//					isPrime = false;
//					break;
//				}
//			}
			if ( isPrime(i) )
			{
				cnt++;
				sum+=i;
			}
		}
		System.out.println("在"+m+"和"+n+"之间有"+cnt+"个素数，总和为"+sum);
		

	}

}
