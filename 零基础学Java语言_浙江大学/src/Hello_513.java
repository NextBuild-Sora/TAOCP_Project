import java.util.Scanner;

/* 第5周 数组
 * 5.1 数组 
 *  5.1.3 数组的元素,
 *  
 */


public class Hello_513 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		double sum = 0;
		int cnt = 0;
		cnt = in.nextInt();
		if ( cnt>0 )
		{
			int [] numbers = new int[cnt];	//定义数组。//			for (int i=0; i<cnt; i++)
			for (int i=0; i<cnt; i++)
			{
				numbers[i] = in.nextInt();
				sum += numbers[i];
			}
			
			double average = sum/cnt;
	//			遍历数组
//			for (int i=0; i<cnt; i++)
			for (int i=0; i<numbers.length; i++)
			{
	//			使用数组中的元素
				if (numbers[i] > average)
				{
					System.out.println("数组：" + numbers[i]);
				}
			}
			System.out.println(" 平均数的值 " + sum/cnt);	//输出平均数的值
		}
	}
}


