import java.util.Scanner;

/* 第5周 数组
 * 5.2 数组计算 
 * 5.2.1 投票统计 
*/

public class Hello_521 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		int x;
		int[] numbers = new int[10];	//创建数组
		for (int i=0; i<numbers.length; i++)
			System.out.println(numbers[i]);
				
		x = in.nextInt();
		while (x!=1)
		{
			if (x>0 && x<9)
			{
				numbers[x] ++;	//数组参与运算
			}
			x = in.nextInt();
		}
//		遍历数组输出
		for (int i=0; i<numbers.length;i++)
		{
			System.out.println(i+":"+numbers[i]);
		}

	}

}
