import java.util.Scanner;

/* 第5周
 * 5.3 二维数组
 * 井字棋
 * 5.3.1_2 
 */

public class Hello_531_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Scanner inScanner = new Scanner(System.in );
		Scanner in = new Scanner(System.in );

		final int size=3;
		int[] state=new int [8];
		boolean [] men=new boolean [2];
		int [][] board= new int [size][size];
		
		//读入
		for(int i=0;i<board.length;i++)
		{
			for(int j=0;j<board[i].length;j++)
			{
				board[i][j]=in.nextInt();
			}
		}
		
		
		//处理
		//行、列
		for(int i=0;i<board.length;i++)
		{
			for(int j=0;j<board[i].length;j++)
			{
				state[i]+=board[i][j];
				state[j+3]+=board[i][j];
			}
		}
		
		//对角线
		for(int i=0;i<board.length;i++)
		{
			state[6]+=board[i][i];
			state[7]+=board[i][size-i-1];
		}
		
		for(int i=0;i<state.length;i++)
		{
			if(state[i]==0||state[i]==3)
		
			{
				if(state[i]==0)
				{
					men[0]=true;
					
				}
				else
				{
					men[1]=true;
					
				}
			}

		}
		if(men[0]||men[1])
		{
			if(men[0])
			{
				System.out.println("0的一方获胜");
			}
			else
			{
				System.out.println("1的一方获胜");
			}
		}
		else
		{
			System.out.println("没人获胜");
		}	
		
	}
}



