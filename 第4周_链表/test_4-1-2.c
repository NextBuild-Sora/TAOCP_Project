/*******************************
 *	---第4周：链表---
 *	--1 可变数组--
 *	-2 可变数组的数据访问-
 *
 *******************************/




#include "test_4-1-1.h"
#include <stdio.h>
#include <stdlib.h>

//typedef struct {
//	int *array;
//	int size;
//} Array;

Array array_create(int init_size)
{
	Array a;
	a.array =  init_size; 
	a.array = (int*)malloc(sizeof(int)*a.size);
	return a;
}

void array_free(Array *a)
{
	free(a->array);
	a->array = NULL; 
	a->size = 0;
}

// 封装
int array_size(const Array *a)
{
	return a->size;
}

int* array_at(Array *a, int index)
{
	return &(a->array[index]);
}

int array_get(const Array *a, int index)
{
	return a->array[index];
}

void array_set(Array *a, int index, int value)
{
	a->array[index] = value;
}

void array_inflate(Array *a, int more_size);

int main(int argc, char const *argv[])
{
	Array a = array_create(100);
	printf("%d\n", array_size(&a));
	*array_at(&a, 0) = 10;
	printf("%d\n", *array_at(&a, 0));
	
	array_free(&a);
	
	return 0;
}


