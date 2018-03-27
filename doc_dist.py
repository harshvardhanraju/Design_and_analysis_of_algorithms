"""
@Harsha
Date : 21/3/18
"""
import re
import sys
import os
import numpy as np

FILE_LOC = os.path.join(os.getcwd(), 'files')


def generate_doc_freq(fl):
    """
    Given a doc, generates word frequency vector for it
    """
    freq_dict = {}
    f = open(fl, 'r')
    text_string = f.read().lower()
    match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
    for word in match_pattern:
        count = freq_dict.get(word, 0)
        freq_dict[word] = count + 1
    return freq_dict


def doc_dist(freq1, freq2):
    norm1 = np.linalg.norm(freq1)
    norm2 = np.linalg.norm(freq2)
    dot_prod = np.dot(freq1, freq2)
    dist = np.arccos(dot_prod / (norm1 * norm2))
    return dist


def generate_vectors(freq1_dict, freq2_dict):
    freq1_vec, freq2_vec = [], []
    for key1 in freq1_dict.keys():
        if key1 in freq2_dict.keys():
            freq1_vec.append(freq1_dict[key1])
            freq2_vec.append(freq2_dict[key1])
        elif key1 not in freq2_dict.keys():
            freq1_vec.append(freq1_dict[key1])
            freq2_vec.append(0)
    for key2 in freq2_dict.keys():
        if key2 not in freq1_dict.keys():
            freq1_vec.append(0)
            freq2_vec.append(freq2_dict[key2])
    return freq1_vec, freq2_vec


if __name__ == "__main__":
    f1_name = sys.argv[1]
    f2_name = sys.argv[2]
    freq1_dict = generate_doc_freq(os.path.join(FILE_LOC, f1_name))
    freq2_dict = generate_doc_freq(os.path.join(FILE_LOC, f2_name))
    freq1, freq2 = generate_vectors(freq1_dict, freq2_dict)
    dist = doc_dist(freq1, freq2)
    print(dist)
