import collections
import re
import sys

def load_data(filepath):
    with open(filepath, "r") as textfile:
        text = textfile.read().lower()
    return text
   
def get_most_frequent_words(text, words_num=10):
    words = re.findall(r'\w+', text)
    count_words = collections.Counter(words).most_common(words_num)
    return count_words
    
if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        text = load_data(filepath)
        count_words = get_most_frequent_words(text)
        print('Список самых часто встречающихся слов:')
        for prettify in count_words:
            print(prettify)
    except IndexError:
        print('Вы не ввели путь до текстового файла')
    
  
