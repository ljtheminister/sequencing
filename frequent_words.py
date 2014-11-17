from pattern_count import pattern_count

def frequent_words(text, k):
    frequent_patterns = set()
    count = []
    N = len(text)
    for i in range(N-k):
        pattern = text[i:i+k]
        count.append(pattern_count(text, pattern))
    max_count = max(count)
    for i in range(N-k):
        if count[i] == max_count:
            frequent_patterns.add(text[i:i+k])
    return frequent_patterns

if __name__ == '__main__':
    with open('dataset_2_9.txt') as f:
        data = f.read()
    data = data.split('\n')
    dna_string = data[0]
    k = int(data[1])
    frequent_k_mers = frequent_words(dna_string, k)
    with open('freq_k_mers.txt', 'w') as outfile:
        outfile.write(" ".join(list(frequent_k_mers))+ '\n')
