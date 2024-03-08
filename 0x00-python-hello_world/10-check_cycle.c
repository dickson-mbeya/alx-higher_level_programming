#include <stdio.h>
#include <stdlib.h>

/* Definition of a singly linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to check if a singly linked list has a cycle */
int check_cycle(listint_t *list) {
    if (list == NULL || list->next == NULL)
        return 0;  // No cycle if the list is empty or has only one node
    
    listint_t *slow = list;
    listint_t *fast = list->next;

    while (fast != NULL && fast->next != NULL) {
        if (slow == fast) {
            return 1;  // Cycle detected
        }
        slow = slow->next;
        fast = fast->next->next;
    }

    return 0;  // No cycle detected
}

/* Example usage */
int main() {
    // Creating a linked list with a cycle for testing
    listint_t *head = malloc(sizeof(listint_t));
    head->n = 1;
    head->next = malloc(sizeof(listint_t));
    head->next->n = 2;
    head->next->next = malloc(sizeof(listint_t));
    head->next->next->n = 3;
    head->next->next->next = head; // Creating a cycle

    // Checking if the linked list has a cycle
    if (check_cycle(head))
        printf("The linked list has a cycle.\n");
    else
        printf("The linked list does not have a cycle.\n");

    // Freeing memory
    free(head->next->next);
    free(head->next);
    free(head);

    return 0;
}
