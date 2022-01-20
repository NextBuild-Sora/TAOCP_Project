

/* 第7周 函数
 * 7.2 函数定义与调用
 * 7.2.2 函数内的变量————本地变量
 * 
 */


public class Hello_722 {
	public static void sum(int a, int b)
	{
		int i;
		int sum;
		sum = 0;
		for ( i=a; i<=b; i++ )
		{
			sum += i;
		}
		System.out.println(a+"到"+b+"的和是"+sum);
		
	}
	
	public static int factor(int i)
	{
		if ( i == 1 )
			return i;
		return i*factor(i-1);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int k = factor(3);
		System.out.println(k);

	}

}
