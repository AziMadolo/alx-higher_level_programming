#include "lists.h"

/**
 * delete_dnodeint_at_index - Deletes the node at the specified index in a
 * dlistint_t linked list.
 * @head: Pointer to the head of the list.
 * @index: Index of the node to be deleted.
 * Return: 1 if successful, -1 if failed.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *current = *head;
    dlistint_t *previous = NULL;
    unsigned int count = 0;

    if (current == NULL)
        return (-1);

    while (current != NULL && count < index)
    {
        previous = current;
        current = current->next;
        count++;
    }

    if (current == NULL)
        return (-1);

    if (previous == NULL)
    {
        *head = current->next;
        if (*head != NULL)
            (*head)->prev = NULL;
    }
    else
    {
        previous->next = current->next;
        if (current->next != NULL)
            current->next->prev = previous;
    }

    free(current);
    return (1);
}
