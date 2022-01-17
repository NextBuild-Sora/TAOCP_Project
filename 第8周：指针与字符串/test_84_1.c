
/******************************
 *
 *	第8周：指针与字符串
 *
 *	-4 字符计算 --
 *	--- 1 字符串输入输出---
 *
 ******************************/


#include <stdio.h>

int main()
{
	char word[8];
	char word2[8];
	scanf("%s", word);
	scanf("%s", word2);
	printf("%s##\n", word);
	printf("%s##\n", word2);
	printf("%s##%s##\n", word, word2);

	return 0;

}
