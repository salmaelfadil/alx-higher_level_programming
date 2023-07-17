#include "lists.h"
/**
 * reverse_listint - revereses an intlist
 * @head: pointer to the head of the list
 *
 * Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *prv = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prv;
		prv = current;
		current = next;
	}

	*head = prev;
}
/**
 * is_palindrome -- checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 *
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *list_dup, *list_s, *list_f, *tmp;
	list_dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	list_s = *head, list_f = *head, tmp = *head;

	while (1)
	{
		list_f = list_f->next->next;
		if (list_f == NULL)
		{
			list_dup = list_s->next;
			break;
		}
		if (list_f->next == NULL)
		{
			list_dup = list_s->next->next;
			break;
		}
		list_s = list_s->next;
	}
	reverse_list(&list_dup);

	while (list_dup && tmp)
	{
		if (tmp->n == list_dup->n)
		{
			list_dup = dup->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}
	if (list_dup == NULL)
		return (1);

	return (0);
}
