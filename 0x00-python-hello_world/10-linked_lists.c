#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * add_nodeint - adds  new node at the begining
 * @head: pointer to a pointer of the start of the list
 * @n: integer included in node
 * Return: NULL at failure or address of the new element
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *add;

    add = malloc(sizeof(listint_t));
    if (add == NULL)
            return (NULL);
    add->n = n;
    add->next = *head;
    *head = add;
    return (add);
}


/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    unsigned int n;
    const listint_t *current;
    n = 0;
    current = h;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}


/**
 * free_listint - frees a list
 * @head: pointer to list to be freed
 * Return: nothing
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
