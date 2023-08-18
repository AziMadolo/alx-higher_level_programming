#ifndef _LISTS_
#define _LISTS_

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *prev;
    struct Node *next;
} Node;

size_t printNodeList(const Node *head);
size_t getNodeListLength(const Node *head);
Node *addNodeToFront(Node **head, const int value);
Node *addNodeToEnd(Node **head, const int value);
void freeNodeList(Node *head);
Node *getNodeAtIndex(Node *head, unsigned int index);
int sumNodeListValues(Node *head);
Node *insertNodeAtIndex(Node **head, unsigned int index, int value);
int deleteNodeAtIndex(Node **head, unsigned int index);

#endif /* _LISTS_ */

