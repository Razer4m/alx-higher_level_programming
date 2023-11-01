#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	current = *head;

	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	
	if (prev == NULL)
	{
		new_node->next = current;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
