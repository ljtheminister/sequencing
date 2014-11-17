import sys
import itertools
import pandas as pd
import numpy as np

'''
def create_lexicon(k):
    lexicon_num_dict = dict(zip(lexicon_list, list(range(4**k))))
    return lexicon_num_dict

k_mer_list = ['A', 'C', 'G', 'T']
symbol_number = dict(zip(k_mer_list, list(range(4))))

def pattern_to_number(pattern):
    if pattern == '':
        return 0
    symbol = pattern[-1]
    pattern = pattern[:-1]
    return 4 * pattern_to_number(pattern[:-1] + symbol_number[symbol])

'''

def computing_frequencies(text, k):
    k_mer_list = ['A', 'C', 'G', 'T']
    arrays = [k_mer_list for i in range(k)]
    lexicon_list = list(itertools.product(*arrays))
    lexicon_list = [''.join(x) for x in lexicon_list]
    freq_array = pd.Series(0, index=lexicon_list)    
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        freq_array.ix[pattern] += 1
    return freq_array
    
if __name__ == '__main__':
    with open('dataset_2994_5.txt') as f:
        data = f.read()
    data = data.split('\n')
    dna_string = data[0]
    k = int(data[1])
    freq_array = computing_frequencies(dna_string, k)
    freq_array = freq_array.apply(lambda x: str(x))
    with open('frequencies.txt', 'w') as outfile:
        outfile.write(' '.join(freq_array.values) + '\n')

