import java.util.Scanner;

/* 第5周 数组
 * 5.1 数组 
 * 5.1.4_2 数组变量 
 */

public class Hello_514_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		int[] a = {1,2,3,4,5};
//		int[] b = {1,2,3,4,5};
//		System.out.println(a==b);
		
		int[] b = new int[a.length];
		for (int i=0; i<b.length; i++)
		{
			b[i] = a[i];
		}
		boolean isEqu = true;
		for (int i=0; i<b.length; i++)
		{
			if (a[i] != b[i])
			{
				isEqu = false;
				break;
			}
//			System.out.println(b[i]);
		}
//		System.out.println(a==b);
		System.out.println(isEqu);
	}

}
