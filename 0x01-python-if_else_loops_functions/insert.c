#include "lists.h"

/**
 * insert_node - Inserts  number into linked list.
 * @head: A pointer the head of the linked list.
 * @number: inserted integer
 *
 * Return: NULL for failure or pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
    listint_t *new;

/**	new = malloc(sizeof(listint_t));*/
	if (new_node == NULL)
		return (NULL);
    new_node = malloc(sizeof(listint_t));
	new_node->n = number;

	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}
