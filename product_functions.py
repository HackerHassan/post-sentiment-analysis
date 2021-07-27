# these are the product related functions
import pandas as pd

def pull_sizes_function(title_list):
    t_list = []
    for curr_title in (title_list):
        curr = curr_title
        if '/' in str(curr):
            split_title = curr.split('/')
            curr = split_title[0]
        t_list.append(curr)
    return t_list

