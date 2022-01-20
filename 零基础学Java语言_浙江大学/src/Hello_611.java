import java.util.Scanner;

/* 第6周 使用对象
 * 6.1 字符类型
 * 6.1.1 字符类型
 */

public class Hello_611 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		char c = 'a';
		char b = '\u0041';
//		char d = 'd';
		char a = 65;
		char d = (char)(c + 'A'-'c');	//大小写转换。
		
//		c++;
//		System.out.println(d-c);
		System.out.println((int)c);
		System.out.println(c);
		System.out.println(a);

		System.out.println('汉'>'A'); 	//大小比较

		System.out.println('A'>'B'); 	//大小比较

		System.out.println('a'>'A'); 	//大小比较



	}

}
