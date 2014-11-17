import sys
import pandas as pd
import numpy as np
from computing_frequencies import computing_frequencies

def faster_frequent_words(text, k):
    frequent_patterns = set()
    frequency_array = computing_frequencies(text, k)
    max_count = max(frequency_array)
    for pattern, count in frequency_array.iteritems():
        if count == max_count:
            frequent_patterns.add(pattern)

