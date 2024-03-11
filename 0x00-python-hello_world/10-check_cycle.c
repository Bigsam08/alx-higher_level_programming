#include "lists.h"

/**
 * check_cycle - check to see if cycle exist
 * Description: @list linked list to check
 *
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *forward = list;
	listint_t *backward = list;

	while (forward && backward && forward->next)
	{
		backward = backward->next;
		forward = forward->next->next;
		if (backward == forward)
			return (1);
	}
	return (0);
}
