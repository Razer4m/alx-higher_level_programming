#include "lists.h"
/**
 * reverse_list - Reverses a singly linked list in place.
 * @head: Pointer to the head of the linked list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the linked list.
 * Return: 1 if it is a palindrome, 0 if it is not.
 * An empty list or a single node list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	listint_t *second_half = reverse_list(slow);

	listint_t *first_half = *head;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			reverse_list(second_half);
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	reverse_list(second_half);
	return (1);
}
