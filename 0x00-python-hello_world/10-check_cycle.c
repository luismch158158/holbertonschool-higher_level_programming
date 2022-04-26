#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked
 * list has a cycle in it
 *
 * @list: pointer to head
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */


int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare = list;

	while (hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;

		if (turtle == hare)
		{
			return (1);
		}
	}
	return (0);
}
