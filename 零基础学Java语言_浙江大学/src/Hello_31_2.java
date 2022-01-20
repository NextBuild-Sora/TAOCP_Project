import java.util.Scanner;

//	《第3周 循环》
//	3.1.2 数数字

public class Hello_31_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//	初始化
		Scanner in = new Scanner(System.in);
		int number = in.nextInt();
		int count = 0;
		while ( number >0 )
		{
			number = number / 10;
			count = count +1;
		}
		System.out.println("位数：" + count);
	}

}
