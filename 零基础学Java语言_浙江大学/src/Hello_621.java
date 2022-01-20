import java.util.Scanner;

/* 第6周 使用对象
 * 6.2 包裹类型
 * 6.2.1 包裹类型
 */


public class Hello_621 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		int i = 10;	//基础类型
		Integer k = 10;	//包裹类型
		k = i;
		
		System.out.println(Integer.MAX_VALUE);	//整数最大值
		
		System.out.println(Character.isDigit('a'));	//判断是否为数字
		
		System.out.println(Character.isLowerCase('a'));	//判断小写
		
		System.out.println(Character.toLowerCase('I'));	//转换小写
	}

}
