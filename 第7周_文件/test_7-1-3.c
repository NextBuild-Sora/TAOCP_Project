/*	
	--第7周：文件--
	--1 文件--
	--3 二进制文件--

 */


#include <stdio.h>
#include "student.h"

/*
void getList(Student aStu[], int number);
int save(Student aStu[], int number);

int main(int argc, char const *argv[]) 
{
	int number = 0;
	printf("输入学生数量：");
	scanf("%d", &number);
	Student aStu[number];
	
	getList(aStu, number);
	if ( save(aStu, number) ) {
		printf("保存成功\n");
	} else {
		printf("保存失败\n");
	}
	
	return 0;
	
}

void getList(Student aStu[], int number)
{
	char format[STR_LEN];
	sprintf(format, "%%%ds", STR_LEN-1);
	//"%19S"
	
	int i;
	for ( i=0; i<number; i++ ) {
		printf("第%d个学生：\n", i);
		printf("\t姓名：");
		scanf(format, aStu[i].name);
		printf("\t年龄：");
		scanf("%d", &aStu[i].age);
	}
}

int save(Student aStu[], int number)
{
	int ret = -1;
	FILE *fp = fopen("student.data", "w");
	if (fp) {
		ret = fwrite(aStu, sizeof(Student), number, fp);
		fclose(fp);
	}
	return ret == number;
}
*/



void read(FILE *fp, int index);

int main(int argc, char const *argv[]) 
{
	FILE *fp = fopen("student.data", "r");
	if (fp) {
		fseek(fp, 0L, SEEK_END);
		long size = ftell(fp);
		int number = size / sizeof(Student);
		int index = 0;
		printf("有%d个数据，你要看第几个：", number);
		scanf("%d", &index);
		read(fp, index-1);
		fclose(fp);
	}
	return 0;
	
}

void read(FILE *fp, int index)
{
	fseek(fp, index*sizeof(Student), SEEK_SET);
	Student stu;
	if ( fread(&stu, sizeof(Student), 1, fp) == 1 ) {
		printf("第%d个学生：", index+1);
		printf("\t姓名：%s\n", stu.name);
		printf("\t性别：");
		switch (stu.gender) {
		case 1: printf("男\n"); break;
		case 2: printf("女\n"); break;
		case 3: printf("其他\n"); break; 
		}
		printf("\t年龄：%d\n", stu.age);
	}
}

int save(Student aStu[], int number)
{
	int ret = -1;
	FILE *fp = fopen("student.data", "w");
	if (fp) {
		ret = fwrite(aStu, sizeof(Student), number, fp);
		fclose(fp);
	}
	return ret == number;
}



