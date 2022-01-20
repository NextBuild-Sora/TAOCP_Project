import java.util.Scanner;

/* 第4周
 * 4.2 循环控制
 * 4.2.2_1 多重循环 
 */


public class Hello_422_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int amount = in.nextInt();
//		int isExist = 0;
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
//							isExist = 1;
							break;	//跳出循环		
						}
					}
//					if (isExist == 1) break;
				}
//				if (isExist == 1) break;
			}
//			if (isExist == 1) break;
		}
	
	}

}
