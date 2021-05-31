from anagram_sets import all_anagrams, print_anagram_sets
import shelve


def store_anagrams(anagrams_dict, pickle_filename):
    database = shelve.open(pickle_filename)
    for key, value in anagrams_dict.items():
        database[key] = value
    database.close()


def read_anagrams(word, pickle_filename):
    sorted_word = sorted(word)
    delimiter = ''
    key = delimiter.join(sorted_word)
    s = shelve.open(pickle_filename)
    result = s[key]
    s.close()
    return result


if __name__ == '__main__':

    anagrams = all_anagrams('/Users/conniecanelon/dev/words.txt')
    store_anagrams(anagrams, 'ANAGRAMS')
    print(read_anagrams('zaniest', 'ANAGRAMS'))


