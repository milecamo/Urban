# Задача "Однокоренные"

def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for word in other_words:
        low_word = word.lower()
        if low_word in root_word or root_word in low_word:
            same_words.append(word)
    return same_words


print('Single root words for rich are:',
      *single_root_words('rich',
                         'richiest', 'orichalcum', 'cheers', 'richies'), '.')
print('Single root words for Disablement are:',
      *single_root_words('Disablement',
                         'Able', 'Mable', 'Disable', 'Bagel'), '.')
print('Single root words for Intro are: '
      f'{", ".join(word for word in
                   single_root_words('Intro',
                                     'int',
                                     'introspective',
                                     'entropy',
                                     'interviajes',
                                     'interview')
                   )
      }.')
