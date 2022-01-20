import java.util.Scanner;

/* 第5周 数组
 * 5.1 数组 
 *  5.1.1 初时数组
 *  这个程序存在安全隐患。。。
 */


public class Hello_511 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int x;
		int [] numbers = new int[100];	//定义数组。
//		numbers[-1] = 10;
//		numbers[100] = 10;
		double sum = 0;
		int cnt = 0;
		x = in.nextInt();
		while(x != -1)
		{
			numbers[cnt] = x;	// 相当于numbers[0]=x; 对数组中的元素赋值。
			sum += x;
			cnt ++;
			x = in.nextInt();
		}
		if (cnt>0);
		{
			double average = sum/cnt;
//			遍历数组
			for (int i=0; i<cnt; i++)
			{
//				使用数组中的元素
				if (numbers[i] > average)
				{
					System.out.println("数组：" + numbers[i]);
				}
			}
			System.out.println(" 平均数的值 " + sum/cnt);	//输出平均数的值
		}

	}

}
