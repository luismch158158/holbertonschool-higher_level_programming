#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    total_a = len(tuple_a)
    total_b = len(tuple_b)

    if (total_a < 2):
        nt_a = tuple_a + (0, 0)
    else:
        nt_a = tuple_a

    if (total_b < 2):
        nt_b = tuple_b + (0, 0)
    else:
        nt_b = tuple_b

    n_t = (nt_a[0] + nt_b[0]), (nt_a[1] + nt_b[1])
    return (n_t)
