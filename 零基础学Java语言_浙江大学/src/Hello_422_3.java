
import java.util.Scanner;

/* 第4周
 * 4.2 循环控制
 * 4.2.2_3 多重循环 
 */


public class Hello_422_3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int amount = in.nextInt();
		OUT:
		for (int one = 0; one <= amount; ++one )
		{
			for (int five = 0; five <= amount/5; ++five)
			{
				for (int ten = 0; ten <= amount/10; ++ten)
				{
					for ( int twenty = 0; twenty <= amount/20; ++twenty )
					{
						if ( one+five*5+ten*10+twenty*20 == amount )
						{
							System.out.println(one+"张1元，"+five+"张5元，"+ten+"张10元，"+twenty+"张20元-->"+amount);
							break OUT;	//跳出循环		
						}
					}
				}
			}
		}
	
	}

}
