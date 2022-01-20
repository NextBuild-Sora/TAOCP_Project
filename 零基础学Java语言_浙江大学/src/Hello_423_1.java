import java.util.Scanner;

/* 第4周
 * 4.2 循环控制
 * 4.2.3_1 逻辑类型 
 */


public class Hello_423_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		if ( !(n > 0) ) 	//逻辑运算符：!优先级（单目）最高
		{
			
		}
		boolean isPrime = true;
//		for (int n =2; n<100; n++)
		{
			for (int i = 2; i<n; i++)
			{
				if (n%i ==0 )
				{
					isPrime = false;
					System.out.println(n+"不是素数，i= "+i);
					break;	//跳出循环
				}
			}
			if (isPrime)
			{
				System.out.println(n+"是素数");
//				System.out.print(n+" ");
			}
			else
			{
				System.out.println(n+"不是素数");
			}
		}
	}

}
