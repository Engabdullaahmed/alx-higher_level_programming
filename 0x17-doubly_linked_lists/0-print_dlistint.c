#include "lists.h"
#include <stdio.h>

/**
 * print_dlistint - print all dlistint list
 * @h: point start of linked list
 * Return: num of nodes
 */


size_t print_dlistint(const dlistint_t *h)
{
size_t i;

for (i = 0; h != NULL; i++)
{
printf("%d\n", h->n);
h = h->next;
}
return (i);
}