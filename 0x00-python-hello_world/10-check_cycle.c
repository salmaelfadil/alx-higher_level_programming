#include "lists.h"
/**
 * check_cycle -- checks if a singly linked list has
 * a cycle in it
 * @list: linked list to be checked
 *
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	if (!list)
		return (0);

	while (ptr1 != NULL && ptr2 != NULL && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr2 == ptr1)
		{
			return (1)
		}
	}
	return (0);
}
