/*******************************
 *	---第3周：结构类型---
 *	--3 联合--
 *	-1 类型定义-
 *
 *******************************/


#include <stdio.h>

int main(int argc, char const *argv[]) 
{
	typedef long int64_t;
	typedef struct ADate{
		int month;
		int day;
		int year;
		
	} Date;
	
	int64_t i = 1000000;
	Date d = {9, 1, 2005};
	
	
	typedef int Length;		//Length就等价与int类型
	
	typedef char* Strings[10];		//Strings是10个字符串的数组的类型
	
	typedef struct node{
		int data;
		struct node *next;
	} aNdoe;
	
	typedef struct node aNode; 	//这样用aNode就可以代替struct node.
	
	return 0;
}




