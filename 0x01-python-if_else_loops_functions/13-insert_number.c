#include "lists.h"

/**
 * insert_node - Function that inserts a number
 * into a sorted singly linked list
 *
 * @head: pointer to pointer head
 * @number: number to add in node
 *
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *before = *head;
	listint_t *after = *head;
	listint_t *temp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	after = after->next;

	while (before && after->next)
	{
		if ((number > (before->n)) && (number < (after->n)))
		{
			new_node->n = number;

			temp = before->next;
			before->next = new_node;
			new_node->next = temp;
		}
		after = after->next;
		before = before->next;
	}

	return (new_node);
}
