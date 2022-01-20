import java.util.Scanner;

/* 第4周
 *  4.3 循环的例子
 *  4.3.1_2 求和
 */


public class Hello_431_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		double sum = 0.0;
		int sign = 1;
		for (int i =1; i<=n; i++, sign = -sign)	//这种方法也可以
		{
			sum += sign*1.0/i;		
		}
//		System.out.println(sum);
		System.out.printf("%.2f", sum);	//取2位小数
	
	}
}

