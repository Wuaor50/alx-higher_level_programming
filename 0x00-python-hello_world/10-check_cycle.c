#include "lists.h"
/**
  * check_cycle -  checks if a singly linked list has a cycle in it
  * @list: pointer to head
  *
  * Return: 1 if it has a cycle else 0
  */
int check_cycle(listint_t *list)
{
	listint_t *temp, *newest;

	if (!list)
	{
		return 0;
	}
	temp = list->next;
	newest = list->next->next;
	while (temp && (temp->next))
	{
		if (temp == newest)
			return (1);
		temp = temp->next;
		newest = newest->next->next
	}
	return (0);
}
