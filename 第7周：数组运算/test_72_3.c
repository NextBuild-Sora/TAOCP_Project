
/******************************
 *
 *	第7周：数组运算
 *
 *	--2 搜索 --
 *	--- 3 二分搜索 ---
 *  
 *******************************/


#include <stdio.h>

int search(int key, int a[], int len)
{
	int ret = -1;
	int left = 0;
	int right = len-1;
	while ( right > left )
	{
		int mid = (left+right)/2;
		if ( a[mid] == k )
		{
			ret = mid;
			break;
			
		} else if ( a[mid]>k )
		{
			right = mid-1;
		} else {
			left = mid+1;
		}
	}
	return -1;
//	return ret;
	
}

int main()
{
	int k = 10;
	int r = search(k, amount, sizeof(amount)/sizeof(amount[0]));

	return 0;
	
}


