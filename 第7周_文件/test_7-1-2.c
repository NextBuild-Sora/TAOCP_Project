/*	
	--第7周：文件--
	--1 文件--
	--2 文件输入输出--

 */


#include <stdio.h>

int main(int argc, char const *argv[])
{
	FILE *fp = fopen("12.in", "r");
	if (fp) {
		int num;
		fscanf(fp, "%d", &num);
		printf("%d\n", num);
		fclose(fp);
	} else {
		printf("无法打开文件\n");
	}
	return 0;
}



