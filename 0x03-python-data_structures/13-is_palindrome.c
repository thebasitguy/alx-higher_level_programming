#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
* add_node_at - pointer to a newly added node to a listint_t
* @head: double pointer to a listint_t
* @n: int value to be stored in the new node
*
* Return: address of the newly added node, or NULL if it failed
*/

listint_t *add_node_at(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
* is_palindrome - checks if a linked list is palindrome
* @head: head of listint_t
*
* Return: 1 if it is palindrome otherwise 0
*/

int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head;
	listint_t *aux = NULL, *aux2 = NULL;

	if (*head == NULL || head2->next == NULL)
		return (1);
	while (head2 != NULL)
	{
		add_node_at(&aux, head2->n);
		head2 = head2->next;
	}
	aux2 = aux;
	while (*head != NULL)
	{
		if ((*head)->n != aux2->n)
		{
			free_listint(aux);
			return (0);
		}
		*head = (*head)->next;
		aux2 = aux2->next;
	}
	free_listint(aux);
	return (1);
}
