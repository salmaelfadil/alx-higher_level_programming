#include "lists.h"
/**
 * is_palindrome -- checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 *
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *head_rev;
	listint_t *current = *head;
	int i = 1;

	head_rev = reverse_list(listint_t **head);

	while (current && head_rev)
	{
		if (current->n == head_rev->n)
			i = 1;
		else:
			i = 0;
		current = current->next;
		head_rev = head_rev->next;
	}

	return (i);
}
/**
 * reverse_list -- revereses an intlist
 * @head: double pointer to head of list
 *
 * Return: listint_t
 */
listint_t reverse_list(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;

	return (head);
}
