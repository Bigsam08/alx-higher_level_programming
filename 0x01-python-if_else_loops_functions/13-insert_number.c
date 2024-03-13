#include <stdlib.h>
#include "lists.h"
#include <unistd.h>

/**
 * insert_node - inserts a number in  linked list
 * @head: double pointer to the linked list
 * @number: number inserted
 *
 * Return: NULL or address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old = NULL;
    listint_t *new = *head;
	listint_t *copy = NULL;

	if (!head)
		return (NULL);

	old = malloc(sizeof(listint_t));
	if (!old)
		return (NULL);
	old->n = number;
	old->next = NULL;

	/***
    if (!*head || (*head)->n > number)
	{
		old->next = *head;
		return (*head = old);
	}
	else
	{
    **/
    while (new && new->n < number)
    {
        copy = new;
        new = new->next;
	
    copy->next = old;
    old->next = new;
	}
    
    if (!*head || (*head)->n > number)
    {
        old->next = *head;
        return (*head = old);
    }

	return (old);
}
