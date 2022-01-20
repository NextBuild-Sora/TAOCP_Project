import java.util.Scanner;

/* 第6周 使用对象
 * 6.3 字符串
 * 6.3.1 字符串变量
 */


public class Hello_631 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		String s = new String("Hello");
		System.out.println(s+" world");
		System.out.println(s+12+24);
		System.out.println(s+(12+24));
		
		String a;
		a = in.nextLine();
		System.out.println(a);
		
		String b;
		b = in.next();	// 读入一个词
		System.out.println(b);
		
	}

}
