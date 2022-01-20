import java.util.Scanner;

/* 第4周
* 4.3 循环的例子
* 4.3.2_1 最大公约数
* 辗转相除法
*/

public class Hello_432_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		int b = in.nextInt();
		int oa = a;
		int ob = b;
		while (b!=0)
		{
			int r = a%b;
			System.out.println(a+","+b+"，余数："+r);	//输入计算
			a = b;
			b = r;
		}
		System.out.println(oa+"和"+ob+"的最大公约数是"+a);
		

	}

}
