# Задача "Найдёт везде"


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            file_data = ''
            with open(file_name, encoding='utf-8') as file:
                file_data = file.read().lower()
            punct_marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
            # punct_marks = [',', '.', '=', '!', '?', ';', ':', ' — '] # should be
            for char in punct_marks:
                file_data = file_data.replace(char, '\r')
            all_words[file_name] = file_data.split()
        return all_words

    def find(self, word):
        word_positions = {}
        low_word = word.lower()
        for file_name, file_words in self.get_all_words().items():
            word_positions[file_name] = file_words.index(low_word) + 1
        return word_positions

    def count(self, word):
        word_counts = {}
        low_word = word.lower()
        for file_name, file_words in self.get_all_words().items():
            word_counts[file_name] = file_words.count(low_word)
        return word_counts


def test(word, result_file, *file_names):
    finder1 = WordsFinder(*file_names)
    result1 = finder1.get_all_words()
    result2 = finder1.find(word)
    result3 = finder1.count(word)
    print(result1)
    print(result2)
    print(result3, end='\n\n')
    if result_file:
        with open(result_file, 'w', encoding='utf-8') as file:
            for res in (result1, result2, result3):
                file.write(str(res))
                file.write('\n')


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'), end='\n\n')  # 4 слова teXT в тексте всего

    test('captain', 'Result for _captain_ in O Captain! My Captain!.txt',
         'Walt Whitman - O Captain! My Captain!.txt')
    test('if', 'Result for _if_ in If.txt',
         'Rudyard Kipling - If.txt')
    test('Child', 'Result for _Child_ in Monday’s Child.txt',
         'Mother Goose - Monday’s Child.txt')
    test('the', 'Result for _the_ in all files.txt',
         'Walt Whitman - O Captain! My Captain!.txt',
         'Rudyard Kipling - If.txt',
         'Mother Goose - Monday’s Child.txt')
