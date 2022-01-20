/* 第7周 函数
 * 7.2 函数参数与函数内的变量
 * 7.2.1 函数的参数
 * 
 */

public class Hello_721 {
	public static int max(double a, int b)
	{
		int ret;
		if ( a>b )
		{
			ret = (int)a;	//类型转换
		}
		else
		{
			ret = b;
		}
		return ret;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int a = 5;
		int b = 6;
		int c;
		c = max(10.0, 12);
		c = max(10, 'a');
		c = max(a,b);
		c = max(a, 23);
		c = max(c,23);
		c = max(max(c,a), 5);
		c = max(max(c,a), max(5,b));
		System.out.println(max(a,b));
		max(12,23);
	}

}
