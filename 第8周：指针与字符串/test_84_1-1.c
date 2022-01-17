
/******************************
 *
 *	第8周：指针与字符串
 *
 *	-4 字符计算 --
 *	--- 1.1 字符串输入输出---
 * 
 ******************************/


#include <stdio.h>


void f(void)
{
	char word[8];
	char word2[8];
	scanf("%7s", word);		//安全的输入
	scanf("%7s", word2);
//	printf("%s##\n", word);
//	printf("%s##\n", word2);
	printf("%s##%s##\n", word, word2);
}

int main()
{
	f();
	
	return 0;
	
}
