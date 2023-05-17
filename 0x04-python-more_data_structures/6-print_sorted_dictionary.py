#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary)
    for ke in sort_dict:
        print(ke + ":", a_dictionary[ke])
