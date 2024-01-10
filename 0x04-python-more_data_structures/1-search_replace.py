#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = list(my_list)
    for k in range(len(n_list)):
        if n_list[k] == search:
            n_list[k] = replace
    return n_list
