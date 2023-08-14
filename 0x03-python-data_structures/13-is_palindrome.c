/*
 * File: 13-is_palindrome.c
 * Auth: Azizipho Madolo
 */

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int check_palindrome(listint_t *left, listint_t *right);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *node = *head, *next, *prev = NULL;
    while (node)
    {
        next = node->next;
        node->next = prev;
        prev = node;
        node = next;
    }

    *head = prev;
    return (*head);
}

/**
 * check_palindrome - Recursive function to check if a list is a palindrome.
 * @left: A pointer to the left node.
 * @right: A pointer to the right node.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int check_palindrome(listint_t *left, listint_t *right)
{
    if (right == NULL)
        return 1;

    int is_sublist_palindrome = check_palindrome(left, right->next) &&
                                (left->n == right->n);

    left = left->next;

    return is_sublist_palindrome;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is a palindrome - 1.
 *         If the linked list is not a palindrome - 0.
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow = *head, *fast = *head, *prev = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        listint_t *temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    if (fast != NULL)
        slow = slow->next;

    int is_palindrome = check_palindrome(prev, slow);
    reverse_listint(&prev);

    return is_palindrome;
}
