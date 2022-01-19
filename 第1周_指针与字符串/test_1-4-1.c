/*
第1周：指针与字符串
	-4 字符串函数的实现-
	-1 函数strlen-

 */


#include <stdio.h>
#include <string.h>

int mylen(const char* s)
{
	
	int idx = 0;
	while(s[idx] != '\0' ) {
		idx++;
		
	}
	return idx;
}

int main(int argc, char const *argv[])
{
	char line[] = "Hello";
//	printf("strlen=%lu\n", strlen(line));
	printf("strlen=%lu\n", mylen(line));
	printf("sizeof=%lu\n", sizeof(line));
	
	return 0;
}


