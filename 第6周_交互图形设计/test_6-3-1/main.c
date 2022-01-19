#include <stdio.h>
#include "acllib.h"

void mouseListener(int x, int y, int button, int event)
{
	printf("x=%d, y=%d, button=%d, event=%d\n", x, y, button, event);
}

int Setup()
{
	initWindow("Test", DEFAULT, DEFAULT, 800, 600);
	initConsole();
	printf("Hello\n");
	int x;
	registerMouseEvent(mouseListener);
	beginPaint();

	line(10, 10, 100, 100);

	endPaint();

	return 0;
}


