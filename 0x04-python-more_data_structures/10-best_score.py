#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None

    best_score = max(a_dictionary, key=lambda k: a_dictionary[k])
    return best_score
