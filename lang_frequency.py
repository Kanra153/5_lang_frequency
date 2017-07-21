import collections
import re
import sys

def load_data(filepath):
    with open(filepath, "r") as textfile:
        text = textfile.read()
    return text
   
def get_most_frequent_words(text):
    words = text.split()
    count = collections.Counter(words).most_common(10)
    return count
    
if __name__ == '__main__':
    filepath = sys.argv[1]
    text = load_data(filepath)
    count = get_most_frequent_words(text)
    print('Список самых часто встречающихся слов:', count)

  