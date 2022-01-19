/*******************************
 *	---第3周：结构类型---
 *	--2 结构--
 *	-3 结构中的结构-
 *
 *******************************/


#include <stdio.h>

struct point{
	int x;
	int y;
};

struct rectangle{
	struct point p1;
	struct point p2;
};

void printRect(struct rectangle r)
{
	printf("<%d, %d> to <%d, %d>\n", r.p1.x, r.p1.y, r.p2.x, r.p2.y);
}

int main(int argc, char const *argv[])
{
	int i;
//	结构中的结构的数组
	struct rectangle rects[] = {
		{{1,2},{3,4}},
		{{5,6},{7,8}}
	};		// 2 rectangles
	for (i=0;i<2;i++) {
		printRect(rects[i]);
	}
}


