import java.util.Scanner;

/* 第5周 数组
 * 5.1 数组 
 *  5.1.4 数组变量
 *  
 */

public class Hello_514 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		int[] scores = {87, 98, 69, 54, 65, 76, 87, 99};
		System.out.println(scores.length);
		for (int i=0; i<scores.length; i++)
		{
			System.out.print(scores[i]+" ");
		}
	}

}
