import java.util.Scanner;

/* 第4周
* 4.3 循环的例子
* 4.3.2 最大公约数
* 枚举
*/

public class Hello_432 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		int b = in.nextInt();
		int gcd=1;
		for (int i=2; i<=a && i<=b; i++)
		{
			if (a%i == 0 && b%i == 0)
			{
				gcd = i;
			}
		}
		System.out.println(a+"和"+b+"的最大公约数是"+gcd);
		

	}

}
