/*******************************
*	---第3周：结构类型---
*	--1 枚举--
*	-1 枚举-
*
*
*******************************/



#include <stdio.h>


/***** 例子1：*****/

//enum COLOR {RED, YELLOW, GREEN};

//int main(int argc, char const *argv[])
//{
//	int color = -1;
//	char *colorName = NULL;
//	
//	printf("输入颜色的代码：");
//	scanf("%d", &color);
//	switch ( color ) {
//	case RED: colorName = "red"; break;
//	case YELLOW: colorName = "yellow"; break;
//	case GREEN: colorName = "green"; break;
//	default: colorName= "unknown"; break;
//	}
//	printf("你喜欢的颜色是：%s\n", colorName);
//	
//	return 0;
//}


/***** 例子2：*****/
//enum color2 {red2, yellow2, green2};
//
//void f(enum color2 c);
//
//int main(void)
//{
//	enum color2 t = red2;
//	
//	scanf("%d", &t);
//	f(t);
//	
//	return 0;
//}
//
//void f(enum color2 c)
//{
//	printf("%d\n", c);
//}


/***** 例子3：枚举量 *****/
enum COLOR3 {RED3=1, YELLOW3, GREEN3=5, NumCOLORS};

int main(int agrc, char const *argv[])
{
	printf("code for REEN is %d\n", GREEN3);
	
	return 0;
}



