#include "lists.h"
/**
 * listint_t -- inserts a number into a sorted
 * singly linked list
 *
 * @head: pointer to head of list
 * @number: number to be added to the list
 *
 * Return: address to new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h = *head;

	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;

	if (h == NULL)
	{
		*head = new;
		new->next = NULL;
		return(new);
	}
	while(h)
	{
		h = h->next;
	}
	if (h->next == NULL)
	{
		h->next = new;
		new->next = NULL;
	}
	return (new);
}
