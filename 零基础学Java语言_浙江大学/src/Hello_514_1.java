import java.util.Scanner;

/* 第5周 数组
 * 5.1 数组 
 * 5.1.4_1 数组变量 
 */

public class Hello_514_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		int[] a = new int[10];
		a[0] = 5;
		int[] b = a;
		System.out.println(a[0]);
		b[0] = 16;
		System.out.println(b[0]);
		System.out.println(a[0]);
		
	}

}
