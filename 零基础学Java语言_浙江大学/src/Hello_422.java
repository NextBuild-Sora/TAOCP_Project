import java.util.Scanner;

/* 第4周
 * 4.2 循环控制
 * 4.2.2 多重循环 
 */


public class Hello_422 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
//		int n = in.nextInt();
		for (int n =2; n<100; n++)
		{
			int isPrime = 1;
			for (int i = 2; i<n; i++)
			{
				if (n%i ==0 )
				{
					isPrime = 0;
//					System.out.println(n+"不是素数");
					break;	//跳出循环
				}
			}
			if (isPrime == 1)
			{
//				System.out.println(n+"是素数");
				System.out.print(n+" ");
			}
			else
			{
				System.out.println(n+"不是素数");
			}
		}
	}

}
