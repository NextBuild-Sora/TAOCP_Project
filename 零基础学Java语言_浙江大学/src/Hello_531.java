//import java.util.Scanner;
//
///* 第5周
// * 5.3 二维数组
// * 5.3.1 
// */
//
//public class Hello_531 {
//
//	public static void main(String[] args) {
//		// TODO Auto-generated method stub
//		Scanner in = new Scanner(System.in);
//		final int SIZE = 3;
//		int[][] board = new int[SIZE][SIZE];
//		boolean gotResult = false;
//		int numOfX = 0;
//		int numOfO = 0;
//		
//		// 读入矩阵
//		//for ( int i=0; i<SIZE; i++)	//一种写法
//		for ( int i=0; i<board.length; i++)	//另一种写法
//		{
//			//for ( int j=0; j<SIZE; j++)
//			for ( int j=0; j<board[i].length; j++)
//			{
//				board[i][j] = in.nextInt();
//			}
//		}
//		
//		// ---检查行---
//		for (int j=0; j<board[i].length; j++)
//		{
//			if ( board[i][j] == 1)
//			{
//				numOfX ++;
//			}
//			else
//			{
//				numOfO ++;
//			}
//		}
//		if ( numOfX == SIZE || numOfO == SIZE )
//		{
//			gotResult = true;
//			break;
//		}
////	}
//	
//		//	检查列
//		if ( !gotResult )
//		{
//			numOfX = 0;
//			numOfO = 0;
//			for ( int j=0; j<SIZE; j++)
//			{
////				if ( board[j][i] == 1)	//报错
//				if (board[j][j] == 1)	//不报错
//				{
//					numOfX ++;
//				}
//				else
//				{
//					numOfO ++;
//				}
//			}
//			if ( numOfX == SIZE || numOfO == SIZE )
//			{
//				gotResult = true;
//				break;	//报错
//			}
//		}
//			
//		// 检查反对角线
//		if ( !gotResult )
//		{
//			numOfX =0;
//			numOfO =0;
//			for ( int i=0; i<SIZE; i++)
//			{
//				if ( board[i][SIZE-i-1] == 1 )
//				{
//					numOfX ++;
//				}
//				else
//				{
//					numOfO ++;
//				}
//			}
//			if (numOfX == SIZE || numOfO == SIZE)
//			{
//				gotResult = true;
//			}
//		}
//		
//		if ( gotResult)
//		{
//			if ( numOfX == SIZE )
//			{System.out.println("某某1赢了");}
//			else
//			{System.out.println("某某2赢了");}
//			
//		}
//	}
//}
//
//
//
