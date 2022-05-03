#include "lists.h"

/**
 * is_palindrome - Function that checks if the linked
 * lists is palindrome
 *
 * @head: double pointer to head
 *
 * Return: 0 if it is not a palindrome
 * 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *start = *head, *final = *head, *holder = NULL;
	int count = 0, analize = 0, i = 0;

	if (*head == NULL)
		return (1);

	for (i = 0; final->next; i++)
	{
		final = final->next;
		count++;
	}

	if (count % 2 != 0)
		count = count - 1;

	while (analize < (count / 2))
	{
		if (start->n != final->n)
			return (0);
		start = start->next;
		holder = start;
		while (holder->next != final)
			holder = holder->next;
		final = holder;
		analize++;
	}
	return (1);
}
