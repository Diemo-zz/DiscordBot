import random

def get_random_member(list_in):
    if not list_in:
        return
    return list_in[random.randint(0, len(list_in)-1)]