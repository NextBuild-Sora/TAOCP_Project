/************************************
 *	---第1周：指针与字符串--
 *	--4 字符串函数的实现--
 *	-4 字符串搜索函数-
 *		
 *
 *************************************/



#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[] )
{
	char s[] = "hello";
	char *p = strchr(s, 'l');
	char c = *p;
	*p = '\0';
	
//	p = strchr(p+1, 'l');	//找第2个。
//	printf("%s\n", p);

//	char *t = (char*)malloc(strlen(p)+1);
//	strcpy(t, p);	
	char *t = (char*)malloc(strlen(s)+1);
	strcpy(t, s);
	printf("%s\n", t);
	free(t);
	
	return 0;
}



