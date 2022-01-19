/*******************************
 *	---第4周：链表---
 *	--2 链表--
 *	-4 链表的搜索 *
 *
 *******************************/


#include "test_4-2-2.h"
#include <stdio.h>
#include <stdlib.h>

//typedef struct _node{
//	int value;
//	struct _node *next;
//} Node;

typedef struct _list {
	Node* head;
	Node* tail;
} List;

void add(Node* head, int number);
void print(List *pList);

int main(int argc, char const *argv[])
{
	List list;
	int number;
	list.head = NULL;
	do {
		scanf("%d", &number);
		if ( number != -1 ) {
			head = add(&list, number);
		}
	} while( number != -1 );
	printf(&list);
	scanf("%d", &number); 
	Node *p;
	int isFound = 0;
	for ( p=list.head; p; p=p->next ) {
		if (p->value == number) {
			printf("找到了\n");
			isFound = 1;
			break;
		}
	}
	if ( !isFound ) {
		printf("没有找到。");
	}
	return 0;
}

void add(List* pList, int number)
{
	// add to linked-list
	Node *p = (Node*)malloc(sizeof(Node));
	p->value = number;
	p->next = NULL;
	// find the last
	Node *last = pList;
	if ( last ) {
		while ( last->next ) {
			last = last->next;
		}
		// attach
		last->next = p;
	} else {
	  pList->head = p;
	}

}

void print(List *pList) {
	Node *p;
	for ( p=pList->head; p; p= p->next ) {
		printf("%d\t", p->value);
	}
	printf("\n");
}



