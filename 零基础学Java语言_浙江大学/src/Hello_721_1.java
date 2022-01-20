/* 第7周 函数
 * 7.2 函数参数与函数内的变量
 * 7.2.1_1 函数的参数
 *  交换
 */

public class Hello_721_1 {
	
	public static void swap(int a, int b)
	{
		int t;
		t = a;
		a = b;
		b = t;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int a = 5;
		int b = 6;
		swap(a,b);
		System.out.println("a= "+a+"；b= "+b);
	}

}
