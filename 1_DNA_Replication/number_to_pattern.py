import itertools
import sys

def create_number_pattern_dict(k):
    k_mer_list = ['A', 'C', 'G', 'T']
    arrays = [k_mer_list for i in range(k)]
    lexicon_list = list(itertools.product(*arrays))
    lexicon_list = [''.join(x) for x in lexicon_list]
    num_pattern_dict = dict(zip(list(range(4**k)), lexicon_list))
    return num_pattern_dict

def number_to_pattern(number, k):
    number_pattern_dict = create_number_pattern_dict(k)
    pattern = number_pattern_dict[number]
    return pattern
