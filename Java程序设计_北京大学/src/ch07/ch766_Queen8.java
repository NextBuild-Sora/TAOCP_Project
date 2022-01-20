

/*
 * 第7章 工具类及常用算法
 * 7.6 常用算法
 *  ---ch766--
 * 回溯
	• 回溯（back-track） 
	• 回溯法也叫试探回溯法
	• 先选择某一可能的线索进行试探，每一步试探都有多种方式，
	将每一方式都一一试探，如果不符合条件就返回纠正，
	反复进行这种试探再返回纠正，直到得出全部符合条件的答案或是问题无解为止。
	
	• 示例 Queen8.java 八皇后问题。
	
	• 回溯法的其本模式：x++; if(…) x--;


*/


package ch07;

public class ch766_Queen8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new ch766_Queen8().solve();

	}
	
	private static final int N = 8; 
	private int[]y; 	//记录每列上的皇后放的位置
	int count = 0; 		//解的个数
	
	public void solve() {
		count = 0;
		y = new int[N+1]; //初始化数组
		int x = 1;
		
		while(x>0)
		{
			y[x]++; //为当前x位置找一个皇后的位置.
			while((y[x]<=N) && (!check(x))) y[x]++; //找到合适的皇后.
			//
			if(y[x]<=N) //找到一个可以放置第x个皇后的位置，到该步为止，所求部分解都满足要求.
			{
				if(x==N) //找到一个完整的放置方案
				{
					count++;
					print();
				}
				else
					x++; //继续寻找下一个皇后的位置，还没找到完整解决方案
			}
			else //未找到可以放置第x个皇后的位置，到该步为止，已经知道不满足要求
			{ 
				y[x] = 0; //因为要回溯，下一次是寻找第x-1个皇后的位置，
				//在下一次确定x-1的位置之后，第x个皇后的开始搜索的位置要重置
				x--; //回溯
			}
		}
	}
		private boolean check( int k ) //测试合法性
		{
			for(int j=1; j<k; j++)
				if( (Math.abs(k-j) == Math.abs(y[j] - y[k]) )
						|| (y[j] == y[k])) return false;
			return true;
		}
		
		private void print() //显示
		{
			System.out.println(count);
			for( int i=1; i<=N; i++)
			{
				for( int j=1; j<+N; j++ )
					if( j==y[i] ) System.out.println("√"); //如果该位置放了皇后则显示√
					else System.out.println("o");
				System.out.println();
				
			}
		
	}

}
