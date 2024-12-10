# Задача "Найдёт везде"

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                file_data = file.read()
                file_data.lower()
                for chr in [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']:
                    file_data.replace(chr, ' ')
                file_words = file_data.split()
                for i in range(len(file_words)):
                    file_words[i] = file_words[i].lower()
                all_words[file_name] = file_words
        return all_words

    def find(self, word):
        word_positions = {}
        low_word = word.lower()
        for file_name, file_words in self.get_all_words().items():
            for i in range(len(file_words)):
                if file_words[i] == low_word:
                    word_positions[file_name] = i + 1
                    break
        return word_positions

    def count(self, word):
        word_counts = {}
        low_word = word.lower()
        for file_name, file_words in self.get_all_words().items():
            word_count = 0
            for file_word in file_words:
                if file_word == low_word:
                    word_count += 1
            word_counts[file_name] = word_count
        return word_counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
