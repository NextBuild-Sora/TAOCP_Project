import java.util.Scanner;

//	《第3周 循环》
//	3.1 循环

public class Hello_31 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		初始化
		Scanner in = new Scanner(System.in);
		
//		读入投币金额
		while (true)
		{
			System.out.println("请投币：");
			int amount = in.nextInt();
			if ( amount >= 10 )
			{
				//打印车票
				System.out.println("********************");
				System.out.println("* Java专线 *");
				System.out.println("* 无指定座位票 *");
				System.out.println("* 票价：10元 *");
				System.out.println("********************");
				//计算并打印找零
				System.out.println("找零：" + (amount-10));
			}


		}
	}

}
