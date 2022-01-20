

/* 第7周 函数
 * 7.1 函数定义与调用
 * 7.1.2_1 函数调用
 * 
 */

public class Hello_712_1 {
	public static int max(int a, int b)
	{
		int ret;
		if ( a>b )
		{
			ret = a;
		}
		else
		{
			ret = b;
		}
		return ret;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub		Scanner in = new Scanner(System.in);
		
		int a = 5;
		int b = 6;
		int c;
		c = max(10,12);
		c = max(a,b);
		c = max(a, 23);
		c = max(c,23);
		c = max(max(c,a), 5);
		c = max(max(c,a), max(5,b));
		System.out.println(max(a,b));
		max(12,23);
	}

}
