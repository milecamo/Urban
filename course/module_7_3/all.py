from module_7_3 import WordsFinder

if __name__ == '__main__':
    finder1 = WordsFinder('All/Walt Whitman - O Captain! My Captain!.txt',
                          'All/Rudyard Kipling - If.txt',
                          'All/Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))
    with open('All/result.txt', 'w', encoding='utf-8') as file:
        file.write(str(finder1.get_all_words()))
        file.write('\n')
        file.write(str(finder1.find('the')))
        file.write('\n')
        file.write(str(finder1.count('the')))
        file.write('\n')

