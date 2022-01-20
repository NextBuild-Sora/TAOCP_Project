import java.util.Scanner;

/* 第5周 数组
 * 5.2 数组计算 
 * 5.2.3 素数 
 * 
*/


public class Hello_523 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int[] primes = new int[50];	//存放数组
		primes[0] = 2;
		int cnt = 1;
		MAIN_LOOP:
		for ( int x = 3; cnt<50; x++)
		{
			for ( int i=0; i<cnt; i++)
			{
				if ( x%primes[i]==0)
				{
					continue MAIN_LOOP;
				}
			}
			primes[cnt++] = x;
		}
		for (int k:primes)
		{
			System.out.print(k+" ");
		}
		
		
	}
}

