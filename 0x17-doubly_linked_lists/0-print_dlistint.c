#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * printNodeList - Prints all the elements of a Node list.
 * @head: Head of the list.
 * Return: The number of nodes.
 */
size_t printNodeList(const Node *head)
{
    size_t count = 0;

    while (head != NULL)
    {
        printf("%d\n", head->value);
        count++;
        head = head->next;
    }

    return count;
}
