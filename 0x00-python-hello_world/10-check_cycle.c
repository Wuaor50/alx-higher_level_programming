#include "lists.h"
/**
  * check_cycle -  checks if a singly linked list has a cycle in it
  * @list: pointer to head
  *
  * Return: 1 if it has a cycle else 0
  */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list->next;
	while (temp)
	{
		if (temp == list)
			return (1);
		temp = list->next
	}
	return (0);
}
