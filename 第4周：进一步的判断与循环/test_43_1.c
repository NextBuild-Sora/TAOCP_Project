/******************************
*
*	第4周
*
*	--3 多路分支---
*	---1---
*
******************************/


#include <stdio.h>

int main()
{
//	int type;
//	scanf("%d", &type);
//	if(type==1)
//		printf("你好");
//	else if (type==2)
//		printf("早上好");
//	else if (type==3)
//		printf("晚上好");
//	else if (type==4)
//		printf("再见");
//	else
//		printf("啊，什么啊？");
	

// ---多路分支---
// 例子1
//	const int MRN = 5;
	int type;
	scanf("%d", &type);
	switch ( type ) {
	case 1:
		printf("你好");
		break;
	case 2:
		printf("早上好");
		break;
	case 3:
		printf("晚上好");
		break;
	case 3+1:
		printf("3+1");
		break;
//	case MRN:
//		printf(" --Ma");
//		break;
	default:
		printf("啊，什么啊？");
		break;
	}
	
//	例子2
//	int i=1;
//	switch ( i%3 ) {
//		case 0: printf("zero");
//		case 1: printf("one");
//		case 2: printf("two");
//	}

	return 0;
	
}



