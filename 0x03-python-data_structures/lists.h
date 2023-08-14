#ifndef LISTS_H
#define LISTS_H

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function prototypes */
void print_list_integer(int *my_list);
int element_at(int *my_list, int idx);
void replace_in_list(int *my_list, int idx, int element);
void print_reversed_list_integer(int *my_list);
void new_in_list(int **my_list, int idx, int element);
void no_c(char *my_string);
void print_matrix_integer(int **matrix);
void add_tuple(int *tuple_a, int *tuple_b, int *result_tuple);
void multiple_returns(char *sentence, int *result);
int max_integer(int *my_list);
int *divisible_by_2(int *my_list);
void delete_at(int **my_list, int idx);
int is_palindrome(listint_t **head);
void print_python_list_info(PyObject *p);

#endif /* LISTS_H */
