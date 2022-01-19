#include "acllib.h"
#include <stdio.h>
//#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

//int main(int argc, char *argv[]) {
//	return 0;
//}


int Setup()
{
	initWindow("Test", DEFAULT, DEFAULT, 800, 600);
	initConsole();
	printf("Hello\n");
	int x;
	
	beginPaint();

	line(10, 10, 100, 100);
	scanf("%d", &x);
	line(100, 100, x, 0);
	
	endPaint();

	return 0;
}


