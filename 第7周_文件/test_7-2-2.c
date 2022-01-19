/*
	7.2.2 移位运算

*/


#include <stdio.h>

int main(int argc, char const *argv[])
{
	unsigned char c = 0xA5; 
	printf("   c=%hhx\n", c);
	printf("c<<2=%d\n", c<<2); 		//左移
	
	int a = 0x80000000;
	unsigned int b = 0x80000000;
	printf("a=%d\n", a);
	printf("b=%u\n", b);
	printf("a>>1=%d\n", a>>1);		//右移
	printf("b>>1=%u\n", b>>1);    
	
	return 0;
}



