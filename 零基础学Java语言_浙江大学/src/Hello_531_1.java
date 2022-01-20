import java.util.Scanner;

/* 第5周
 * 5.3 二维数组
 * 井字棋
 * 5.3.1_1 
 */

public class Hello_531_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner inScanner = new Scanner(System.in );

		final int SIZE = 3;

		int[][]board = new int[SIZE][SIZE];

		int numOfX = 0;

		int numOfO = 0;

		boolean gotResult = false;

		

//		读入矩阵

		for(int i=0; i<board.length; i++)

		{

			for(int j=0; j<board[i].length; j++)

			{

				board[i][j]=inScanner.nextInt();

			}

		}

//		检查行

		for(int i=0; i<board.length; i++)

		{

			numOfX = 0;

			numOfO = 0;

			for(int j=0; j<board[i].length; j++)

			{

				if(board[i][j]==1)

					{

					numOfX++;

					}

				else 

					{

					numOfO++;

					}

			}

			if(numOfO==SIZE||numOfX==SIZE)

			{

				gotResult = true;

				break;

			}

		}

		if(numOfO==SIZE)

		{

			System.out.println("恭喜O获胜！");

		}

		else if(numOfX==SIZE)

		{

			System.out.println("恭喜X获胜！");

		}

//		检查列

		for(int j=0; j<board.length; j++)

		{

			numOfX = 0;

			numOfO = 0;

			for(int i=0; i<board.length; i++)

			{

				if(board[i][j]==1)

					{

					numOfX++;

					}

				else 

					{

					numOfO++;

					}

			}

			if(numOfO==SIZE||numOfX==SIZE)

			{

				gotResult = true;

				break;

			}

		}

		if(numOfO==SIZE)

		{

			System.out.println("恭喜O获胜！");

		}

		else if(numOfX==SIZE)

		{

			System.out.println("恭喜X获胜！");

		}

//		检查对角线（一层循环）

		numOfX = 0;

		numOfO = 0;

		for(int i=0,j=0;i<board.length; i++,j++)

		{

			if(board[i][j]==1)

				{

				numOfX++;

				}

			else 

				{

				numOfO++;

				}

		    if(numOfO==SIZE||numOfX==SIZE)

			{

				gotResult = true;

				break;	

			}

		}

		if(numOfO==SIZE)

		{

			System.out.println("恭喜O获胜！");

		}

		else if(numOfX==SIZE)

		{

			System.out.println("恭喜X获胜！");

		}

		numOfX = 0;

		numOfO = 0;

		for(int i=2,j=0;i>=0;i=i-1,j++)

		{

			if(board[i][j]==1)

				{

				numOfX++;

				}

			else 

				{

				numOfO++;

				}

		    if(numOfO==SIZE||numOfX==SIZE)

			{

				gotResult = true;

				break;	

			}

		}

		if(numOfO==SIZE)

		{

			System.out.println("恭喜O获胜！");

		}

		else if(numOfX==SIZE)

		{

			System.out.println("恭喜X获胜！");

		}
	
		
	}
}



