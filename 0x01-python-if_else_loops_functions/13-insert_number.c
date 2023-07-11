#include "lists.h"
/**
 * insert_node -- inserts a number into a sorted
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

	if (h == NULL || h->n >= number)
	{
		new->next = h;
		*head = new;
		return (new);
	}
	while (h && h->next && h->next->n < number)
	{
		h = h->next;
	}

	h->next = new;
	new->next = NULL;
	return (new);
}
