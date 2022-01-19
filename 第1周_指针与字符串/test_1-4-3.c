/************************************
*	---第1周：指针与字符串--
*	--4 字符串函数的实现--
*	-3 函数strcpr-
*		-字符串拷贝-
*
*************************************/


#include <stdio.h>
#include <string.h>


int mycpy( char* dst, const char* src )
{
	//数组版本
//	int idx = 0;
//	while(src[idx] ){	
//		dst[idx] = src[idx];
//		idx++;
//	}
//	dst[idx] = '\0';

	//指针版本
	char* ret = dst;
	while(*src ){	
		*dst++ = *src++;

	}
	*dst = '\0';
	
//	return dst;
	return ret;
}

int main(int argc, char const *argv[])
{
	char s1[] = "abc";
	char s2[] = "abc";
	strcpy(s1,s2);
	
	return 0;
}


