/*******************************
 *	---第3周：结构类型---
 *	--2 结构--
 *	-2 结构与函数-
 *
 *******************************/


#include <stdio.h>


/*
// 方案一
struct point {
	int x;
	int y;
};

void getStruct(struct point);
void output(struct point);

int main(int argc, char const *argv[])
{
	struct point y= {0, 0};
	getStruct(y);
	output(y);
}

void getStruct(struct point p)
{
	scanf("%d", &p.x);
	scanf("%d", &p.y);
	printf("%d, %d", p.x, p.y);
}

void output(struct point p)
{
	printf("%d, %d", p.x, p.y);
}
*/


/*
// 方案二
struct point {
	int x;
	int y;
};

struct point getStruct(void);
void output(struct point);

int main(int argc, char const *argv[])
{
	struct point y= {0, 0};
	y = getStruct();
	output(y);
}

struct point getStruct(void)
{
	struct point p;
	scanf("%d", &p.x);
	scanf("%d", &p.y);
	printf("%d, %d", p.x, p.y);
	return p;
}

void output(struct point p)
{
	printf("%d, %d", p.x, p.y);
}
*/


// 方案三
struct point {
	int x;
	int y;
};

struct point* getStruct(struct point*);
void output(struct point);
void print(const struct point *p);

int main(int argc, char const *argv[])
{
	struct point y= {0, 0};
	getStruct(&y);
	output(y);
	output(*getStruct(&y));
	printf(getStruct(&y));
	getStruct(&y)->x = 0;
	*getStruct(&y) = (struct point){1, 2}; 
}

struct point* getStruct(struct point *p)
{
	scanf("%d", &p->x);
	scanf("%d", &p->y);
	printf("%d, %d", p->x, p->y);
	return p;
}

void output(struct point p)
{
	printf("%d, %d", p.x, p.y);
}

void print(const struct point *p)
{
	printf("%d, %d", p->x, p->y);
}



