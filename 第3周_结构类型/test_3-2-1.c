/*******************************
 *	---第3周：结构类型---
 *	--2 结构--
 *	-1 结构类型-
 *
 *
 *******************************/



#include <stdio.h>

struct date{
	int month;
	int day;
	int year;
};

int main(int argc, char const *argv[])
{
// 例子1
//	struct date today;
//	today.month = 07;
//	today.day = 31;
//	today.year = 2014;

// 例子2：结构初始化
//	struct date today = {07,31,2014};
//	struct date thismonth = {.month=7, .year=2014};

//	例子3：结构运算
	struct date today;
	today = (struct date){07,31,2014};
	struct date day;
	day = today;
	day.year = 2015;
	
//	例子4
	struct date *pDate = &today;
	printf("address of today is %p\n", pDate);
	
	printf("Today's date is %i-%i-%i. \n",
		today.year, today.month, today.day);
	printf("This month is %i-%i-%i. \n",
//		thismonth.year, thismonth.month, thismonth.day
		day.year, day.month, day.day
		);

	return 0;
}



