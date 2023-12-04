#include "lists.h"
/**
 * palindrome - checks if a singly linked list is a palindrome
 *@head: head list
 *Return: 0 if its not a palindrome, 1 if it is a palindrome
 */
int palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palindrome(head, *head));
}

/**
 * aux_palindrome - aux function
 *@head: head list
 *@tail: tail list
 *Return: 0 if its not a palindrome, 1 if it is a palindrome
 */
int aux_palindrome(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);
	if (aux_palindrome(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
