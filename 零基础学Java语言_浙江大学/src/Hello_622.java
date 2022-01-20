import java.util.Scanner;

/* 第6周 使用对象
 * 6.2 包裹类型
 * 6.2.2 Math类
 */


public class Hello_622 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		
		System.out.println(Math.abs(-12));	//数学函数，求绝对值.
		System.out.println(Math.round(10.645));	//四舍五入
		System.out.println(Math.random());	//随机数
		System.out.println(Math.random()*100);	//0到100之间的随机数
		System.out.println(Math.pow(2, 3.2));	//次方运算
		
	}

}
