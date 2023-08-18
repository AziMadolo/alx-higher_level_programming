#include "lists.h"

/**
 * add_dnodeint - Adds a new node at the beginning
 *               of a dlistint_t list.
 *
 * @head: Pointer to the head of the list.
 * @n: Value of the new element.
 * Return: Address of the new element.
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
    dlistint_t *new_node;
    dlistint_t *first_node;

    new_node = malloc(sizeof(dlistint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = n;
    new_node->prev = NULL;
    first_node = *head;

    if (first_node != NULL)
    {
        while (first_node->prev != NULL)
            first_node = first_node->prev;
    }

    new_node->next = first_node;

    if (first_node != NULL)
        first_node->prev = new_node;

    *head = new_node;

    return (new_node);
}
