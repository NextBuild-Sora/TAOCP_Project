import java.util.Scanner;

/* 第6周 使用对象
 * 6.3 字符串
 * 6.3.2_1 字符串操作
 */


public class Hello_632_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		String s1 = "abc";
//		System.out.println(s1.charAt(0));
//		System.out.println(s1.charAt(3));
		for ( int i=0; i<s1.length(); i++)
		{
			System.out.println(s1.charAt(i));
		}
		
		

	}
}
