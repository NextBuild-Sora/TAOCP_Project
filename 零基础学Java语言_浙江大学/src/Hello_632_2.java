import java.util.Scanner;

/* 第6周 使用对象
 * 6.3 字符串
 * 6.3.2_2 字符串操作
 */


public class Hello_632_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		String s1 = "01234567abc";
		System.out.println(s1.substring(2));
		System.out.println(s1.substring(2, 4));
		
		System.out.println(s1.indexOf('4'));
		System.out.println(s1.indexOf('A'));
		
		String s2 = "0123A56389汉字";
		int loc = s1.indexOf('3');
		System.out.println(s2.indexOf('3', loc+1));
		System.out.println(s2.indexOf("A56"));



	}
}
