import sys
import re
from collections import Counter

if len(sys.argv) < 2:
    print('usage: bow.py <input file> <output file>')
    sys.exit(1)


def is_markup_line(line):
    """
    Returns True if it is markup line
    """

    # TODO: add code to detect markup lines

    return False


def split_to_words(line):
    """
    line - text (without newline chars)
    Returns list of words.
    """

    # TODO: add code to split line into words

    return ['qqq']


def bigrams(words):
    """
    words - list of words
    Returns list of word bigrams.
    Bigram is represented as Python tuple
    """

    # TODO: add code to create list of word bigrams

    return [('hello', 'world')]


def trigrams(words):
    """
    words - list of words
    Returns list of word trigrams.
    Trigram is represented as Python tuple
    """

    # TODO: add code to create list of word trigrams

    return []


def char_bigrams(words):
    """
    words - list of words
    Returns list of char bigrams.
    Bigram is represented as Python tuple
    """

    # TODO: add code to create list of char bigrams

    return []


def char_trigrams(words):
    """
    words - list of words
    Returns list of char trigrams.
    Trigram is represented as Python tuple
    """

    # TODO: add code to create list of char trigrams

    return [('a', 'c', 'c')]


def save_csv(csv_name, counter, formatter=None):
    if formatter is None:
        def formatter(v): return v

    with open(csv_name, 'w') as fout:
        for elem, count in counter.most_common():
            fout.write(f'"{formatter(elem)}",{count}\n')


def format_tuple(v):
    return " ".join(v)


text_lines = []
for line in open(sys.argv[1]):
    line = line.strip()
    if not is_markup_line(line):
        text_lines.append(line)

words = split_to_words(" ".join(text_lines).lower())

out_name = sys.argv[2]
save_csv(out_name, Counter(words))
save_csv(f"2gram-{out_name}", Counter(bigrams(words)), format_tuple)
save_csv(f"3gram-{out_name}", Counter(trigrams(words)), format_tuple)
save_csv(f"char-2gram-{out_name}", Counter(char_bigrams(words)), format_tuple)
save_csv(f"char-3gram-{out_name}", Counter(char_trigrams(words)), format_tuple)

