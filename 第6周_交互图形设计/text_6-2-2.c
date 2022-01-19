/*
	--第6周--
	--2 函数指针及其应用--
	--2 函数指针的使用--
*/


#include <stdio.h>

void f(int i)
{
	printf("in f()， %d\n", i);
}

//	例子2
void g(int i)
{
	printf("in g()， %d\n", i); 
}
void h(int i)
{
	printf("in h()， %d\n", i);  
}


int main(void) 
{
	/* 例子1
	int i = 0;
	int *p = &i;
	* p = 20;
	int a[] = {1,2};
	void (*pf)(int) = f;
	f(20);
	(*pf)(10); 
	printf("%p\n", main);
	printf("%p\n", pf); 
	printf("%p\n", a); 
	*/
	
//	例子2
	int i = 0;
	void (*fa[])(int) = {f,g,h};
	
	scanf("%d", &i);
	if ( i>=0 && i<sizeof(fa)/sizeof(fa[0])) {
		(*fa[i])(0); 
	}
//	switch(i)
//	{
//		case 0:f(0); break;
//		case 1:g(0); break;
//		case 2:h(0); break;
//	}
//	if(i==0){
//		f(0);
//	} else if (i==1) {
//		g(0);
//	}
	
	return 0;
}


