import sys
import itertools

def create_lexicon(k):
    k_mer_list = ['A', 'C', 'G', 'T']
    arrays = [k_mer_list for i in range(k)]
    lexicon_list = list(itertools.product(*arrays))
    lexicon_list = [''.join(x) for x in lexicon_list]
    lexicon_num_dict = dict(zip(lexicon_list, list(range(4**k))))
    return lexicon_num_dict

def pattern_to_number(pattern):
    k = len(pattern)
    lexicon = create_lexicon(k)
    return lexicon[pattern]

if __name__ == '__main__':
    pattern = sys.stdin.readline().split()[0]
    print (pattern_to_number(pattern))
