
/* 6.3.2 图形交互消息 */


#include <stdio.h>
#include "acllib.h"

void mouseListener(int x, int y, int button, int event)
{
	static int ox = 0;
	static int oy = 0;
	printf("x=%d, y=%d, button=%d, event=%d\n", x, y, button, event);
	beginPaint();
	line(ox, oy, x,y); 
	endPaint();
	ox = x; oy = y;
}

void keyListener(int key, int event)
{
	printf("key=%d, event=%d\n", key, event);
}

void timerListener(int id)
{
	static int cnt = 0;
	printf("id=%d\n", id);
	if ( id==0 )
	{
		cnt++;
		if ( cnt==5 )
				CancelTimer(0);
	}
}

int Setup()
{
	initWindow("Test", DEFAULT, DEFAULT, 800, 600);
	initConsole();
	printf("Hello\n");
	int x;
	
	registerMouseEvent(mouseListener);
	registerKeyboardEvent(keyListener);
	registerTimerEvent(timerListener);
	startTimer(0, 500);
	startTimer(1, 1000);
	
	beginPaint();

	line(10, 10, 100, 100);

	endPaint();

	return 0;
}


