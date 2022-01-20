import java.util.Scanner;

/* 第5周 数组
 * 5.2 数组计算 
 * 5.2.3_1 素数 
 * 
*/


public class Hello_523_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		boolean[] isPrime= new boolean[100];
		for (int i=0; i<isPrime.length; i++)
		{
			isPrime[i] = true;
		}
		for ( int i=2; i<isPrime.length; i++)
		{
			for ( int k =2; i*k<isPrime.length; k++)
			{
				isPrime[i*k] = false;
			}
		}
		for ( int i=2; i<isPrime.length; i++ )
		{
			if ( isPrime[i] );
			{
				System.out.print(i+" ");
			}
		}
		
	}
}

