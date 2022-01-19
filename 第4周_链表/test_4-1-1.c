/*******************************
 *	---第4周：链表---
 *	--1 可变数组--
 *	-1 可变数组-
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

int array_size(const Array *a);
int* array_at(Array *a, int index);
void array_inflate(Array *a, int more_size);

int main(int argc, char const *argv[])
{
	Array a = array_create(100);
	array_free(&a);
	return 0;
}


