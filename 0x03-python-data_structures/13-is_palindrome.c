#include "lists.h"


/**
 * check_palindrome - Function that check palindrome recursion
 *
 * @head: pointer to head
 * @final: pointer to node
 *
 * Return: NULL if not is palindrome
 */

listint_t *check_palindrome(listint_t *head, listint_t *final)
{
	if (final->next)
		head = check_palindrome(head, final->next);

	if (!head || head->n != final->n)
		return (0);

	if (head->next)
		head = head->next;

	return (head);
}

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
	listint_t *final = *head;

	if (head == NULL || *head == NULL)
		return (1);

	if (check_palindrome(*head, final) == 0)
		return (0);

	return (1);
}
