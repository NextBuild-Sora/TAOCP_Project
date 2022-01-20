import java.util.Scanner;

//	《第3周 循环》
//	3.1.4 do——while循环

public class Hello_31_4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//	初始化
		Scanner in = new Scanner(System.in);
		int number = in.nextInt();
		int count = 0;
		do
		{
			number = number / 10;
			count = count +1;
			System.out.println("number= "+number+ "; count= "+count);
		}while ( number >0 );
			
		System.out.println("位数：" + count);
	}

}
