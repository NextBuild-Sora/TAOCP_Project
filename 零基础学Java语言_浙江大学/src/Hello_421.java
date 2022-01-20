import java.util.Scanner;

/* 第4周
 * 4.2 循环控制
 * 4.2.1 循环控制 
 */


public class Hello_421 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int isPrime = 1;
		for (int i = 2; i<n; i++)
		{
			if (n%i ==0 )
			{
				isPrime = 0;
				System.out.println(n+"不是素数，i= "+ i);
				break;	//跳出循环
			}
		}
		if (isPrime == 1)
		{
			System.out.println(n+"是素数");
		}
		else
		{
			System.out.println(n+"不是素数");
		}
	}

}
