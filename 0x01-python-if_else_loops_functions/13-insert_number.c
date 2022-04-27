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
	listint_t *new_node = NULL;
	listint_t *evaluation = *head;
	listint_t *temp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	
	new_node->n = number;

	if (head == NULL)
	{
		new_node->next = NULL;
        	*head = new_node;
        	return (*head);
	}
		if (number <= (evaluation->n))
		{
			new_node->next = *head;
			*head = new_node;
			return (*head);
		}

		else
		{
			while (evaluation->next)
			{
				if (number <= (evaluation->n))
				{
					temp = evaluation->next;
					evaluation->next = new_node;
					new_node->next = temp;
					return (new_node);
				}
				evaluation = evaluation->next;
			}
			temp = evaluation->next;
			evaluation->next = new_node;
			new_node->next = temp;
			return (*head);

		}
}
