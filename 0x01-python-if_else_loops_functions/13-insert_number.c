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
	listint_t *new_node = NULL, *evaluation = *head, *after = NULL;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		new_node->next = NULL, *head = new_node;
		return (*head);
	}
	if (number <= (evaluation->n))
	{
		new_node->next = *head, *head = new_node;
		return (*head);
	}
	after = evaluation->next;
	while (evaluation)
	{
		if (after == NULL)
		{
			evaluation->next = new_node;
			break;
		}
		else if (number == (after->n))
		{
			evaluation->next = new_node, new_node->next = after;
			break;
		}
		else if ((after->n > number) && (evaluation->n < number))
		{
			evaluation->next = new_node, new_node->next = after;
			break;
		}
		after = after->next, evaluation = evaluation->next;
	}
	return (*head);
}
