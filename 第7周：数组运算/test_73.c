
/******************************
 *
 *	第7周：数组运算
 *
 *	--3 排序初步--
 *	---  ---
 *
 *******************************/



#include <stdio.h>

int max(int a[], int len)
{
	int maxid = 0;
	for ( int i=1; i<len; i++ )
	{
		if ( a[i] > a[maxid] )
		{
			maxid = i;
		}
	}
	return maxid;
}

int main()
{
	int a[] = {2,45,6,12,87,34,90,24,23,11,65};
	int len = sizeof(a)/sizeof(a[0]);

	int maxid = max(a, sizeof(a)/sizeof(a[0]));
//	printf("%d\n", maxid);
	//swap a[maxid], a[len-1]
	int t = a[maxid];
//	a[maxid] = a[sizeof(a)/sizeof(a[0])-1];
//	a[maxid] = a[sizeof(a)/sizeof(a[0])-1] = t;
	a[maxid] = a[len-1];
	a[len-1] = t;
	printf("%d\n", maxid);


	return 0;

}


