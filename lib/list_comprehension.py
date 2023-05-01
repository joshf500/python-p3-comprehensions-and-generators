#!/usr/bin/env python3

def return_evens(num_list):
    pass
    evenlist=[]
    for i in range (len(num_list)):
        if (num_list[i]%2)==0:
            evenlist.append(num_list[i])
    return evenlist

def make_exclamation(sentence_list):
    pass
    for i in range (len(sentence_list)):
        sentence_list[i]=sentence_list[i]+"!"
    return sentence_list
