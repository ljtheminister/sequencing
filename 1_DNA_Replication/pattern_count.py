def pattern_count(text, pattern):
    count = 0
    k = len(pattern)
    for i in range(len(text)-k):
        if text[i:i+k] == pattern:
            count += 1
    return count

if __name__ == '__main__':
    with open('dataset_2_6.txt') as f:
        data = f.read()
    data = data.split('\n')
    dna_string = data[0]
    pattern = data[1]
    count = str(pattern_count(dna_string, pattern))
    with open('sub', 'w') as f:
        f.write(count)
