#include "lists.h"

/**
 * check_cycle - checks linked list for a cycle
 * @list: linked list
 *
 * Return: 1 if list has a cycle or 0 if otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
