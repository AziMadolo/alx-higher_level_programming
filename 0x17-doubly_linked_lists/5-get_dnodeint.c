#include "lists.h"

/**
 * get_dnodeint_at_index - Returns the nth node of a dlistint_t linked list.
 * @head: Pointer to head of the list
 * @index: Index of the node to search for, starting from 0
 * Return: nth node or NULL
 **/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
    unsigned int counter;
    dlistint_t *temp;

    counter = 0;
    temp = head;

    while (temp)
    {
        if (counter == index)
            return (temp);
        counter++;
        temp = temp->next;
    }

    return (NULL);
}
