
/******************************
 *
 *	第7周：数组运算
 *
 *	--2 搜索 --
 *	--- 1 线性搜索 ---
 *
 *******************************/


#include <stdio.h>

int search(int key, int a[], int len)
{
	int ret = -1;
	for (int i=0; i<len; i++) 
	{
		if ( key == a[i]) 
		{
			ret = i;
			break;
		}
	}
	return ret;
}

int main()
{
	int a[] = {1,3,2,5,12,14,23,6,9,45};
	int r = search(11, a, sizeof(a)/sizeof(a[0]));
	printf("%d\n", r);
	
	return 0;
}


