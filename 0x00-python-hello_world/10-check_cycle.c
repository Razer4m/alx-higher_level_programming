#inlcude "lists.h"

**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 * Return: 1 if there is a cycle, 0 if there is no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL)
	{
		return (0);
	}
	tortoise = list;
	hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			return (1); /* Cycle detected */
		}
	}
	return (0); /* No cycle found */
}
