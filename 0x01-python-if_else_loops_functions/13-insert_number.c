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

	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	while(head)
	{
		head = head->next;
	}
	if (head->next == NULL)
	{
		head->next = new;
		new->n = number;
		new->next = NULL;
	}
	return (new);
}
