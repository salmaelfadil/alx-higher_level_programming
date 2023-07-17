#include "lists.h"
/**
 * is_palindrome -- checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 *
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *list_rev;
	listint_t *current;
	listint_t *mid_node;
	size_t n, i = 0;

	if(!(*head) || !(*head)->next)
		return (1);
	
	current = *head;
	
	while (current)
	{
		n++;
		current = current->next;
	}
	current = *head;
	for (; i < (n / 2) - 1; i++)
	{
		current = current->next;
	}
	if ((n % 2) == 0 && curent->n != current->next->n)
	{
		return (0);
	}
	current = current->next->next;
	list_rev = reverse_list(&current);
	mid_node = list_rev;
	current = *head;
	while (list_rev)
	{
		if (current->n != rev->n)
			return (0);
		current = current->next;
		rev_list = rev_list->next;
	}
	reverse_list(&mid_node);
	return (1);
}
/**
 * reverse_list -- revereses an intlist
 * @head: double pointer to head of list
 *
 * Return: listint_t
 */
listint_t *reverse_list(listint_t **head)
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
