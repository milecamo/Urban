from module_7_3 import WordsFinder

if __name__ == '__main__':
    finder1 = WordsFinder('Rudyard Kipling - If.txt')
    print(finder1.get_all_words())
    print(finder1.find('if'))
    print(finder1.count('if'))
    with open('Rudyard Kipling - If/result.txt', 'w', encoding='utf-8') as file:
        file.write(str(finder1.get_all_words()))
        file.write('\n')
        file.write(str(finder1.find('the')))
        file.write('\n')
        file.write(str(finder1.count('the')))
        file.write('\n')

