#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ses in matrix:
        for save in ses:
            print("{:d}".format(save), end=" " if save != ses[-1] else "")
        print()
