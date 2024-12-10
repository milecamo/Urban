# Задача "Найдёт везде"

import time


class WordsFinder:
    __file_words = None  # for efficient recursive code part

    def __init__(self, *file_names):
        self.file_names = file_names

    # for efficient code part
    # recursive split list of lists and strings
    def __split_words(self, sep=None):
        for i in range(len(self.__file_words)):
            if isinstance(self.__file_words[i], str):
                # split string to list
                if sep:
                    self.__file_words[i] = self.__file_words[i].split(sep)
                else:
                    self.__file_words[i] = self.__file_words[i].split()
            elif isinstance(self.__file_words[i], list):
                # recursive call for list
                old__file_words = self.__file_words

                self.__file_words = old__file_words[i]
                self.__split_words(sep)

                self.__file_words = old__file_words

    # for efficient code part
    # make list of strings from recursive list of lists and strings
    def __integrate_words(self):
        new_file_words = []
        # for i in range(len(self.__file_words)):
        for file_words in self.__file_words:
            if isinstance(file_words, list):
                self.__file_words = file_words
                self.__integrate_words()
                for word in self.__file_words:
                    new_file_words.append(word)
            elif isinstance(file_words, str) and file_words:
                new_file_words.append(file_words.lower())
        self.__file_words = new_file_words

    def get_all_words(self, efficient=None):
        start_time = time.time()
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                file_data = file.read()
                punct_marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
                if efficient:
                    # efficient code
                    # first split on ' - '
                    self.__file_words = file_data.split(punct_marks[len(punct_marks) - 1])
                    # then split on any whitespace
                    self.__split_words()
                    # then split on other punctuation marks
                    for i in range(len(punct_marks) - 1):
                        self.__split_words(punct_marks[i])
                    # make list of strings from recursive list of lists and strings
                    self.__integrate_words()
                    all_words[file_name] = self.__file_words
                else:
                    # simple code
                    file_data = file_data.lower()
                    for chr in punct_marks:
                        file_data = file_data.replace(chr, ' ')
                    all_words[file_name] = file_data.split()
        if efficient != None:
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Время выполнения: {execution_time} секунд. Efficient is {efficient}")
        return all_words

    def find(self, word, efficient=None):
        word_positions = {}
        low_word = word.lower()
        for file_name, file_words in self.get_all_words(efficient).items():
            for i in range(len(file_words)):
                if file_words[i] == low_word:
                    word_positions[file_name] = i + 1
                    break
        return word_positions

    def count(self, word, efficient=None):
        word_counts = {}
        low_word = word.lower()
        for file_name, file_words in self.get_all_words(efficient).items():
            word_count = 0
            for file_word in file_words:
                if file_word == low_word:
                    word_count += 1
            word_counts[file_name] = word_count
        return word_counts


def test(word, result_file, *file_names):
    finder1 = WordsFinder(*file_names)
    print(finder1.get_all_words())
    print(finder1.find(word))
    print(finder1.count(word))
    if result_file:
        with open(result_file, 'w', encoding='utf-8') as file:
            file.write(str(finder1.get_all_words(False)))
            file.write('\n')
            file.write(str(finder1.find(word, True)))
            file.write('\n')
            file.write(str(finder1.count(word)))
            file.write('\n')


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words(False))  # Все слова
    print(finder2.find('TEXT', True))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    test('captain', 'Result - O Captain! My Captain!.txt', 'Walt Whitman - O Captain! My Captain!.txt')
    test('if', 'Result - If.txt', 'Rudyard Kipling - If.txt')
    test('Child', 'Result - Monday’s Child.txt', 'Mother Goose - Monday’s Child.txt')
    test('the', 'Result - all.txt',
         'Walt Whitman - O Captain! My Captain!.txt',
         'Rudyard Kipling - If.txt',
         'Mother Goose - Monday’s Child.txt')
