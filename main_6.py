list_words = []

def read(): # Читаем файл
    with open('words.txt') as f:
        return [word for line in f for word in line.split()] # Делим текст на строки, а далее превращаем все в массив слов

def swap():
    SKIP_WORD = 1 # Константа для лучшей читаемости кода, которая обозначает, что мы пропустим 1 слово в списке
    SKIP_COUPLE_WORDS = 2 # Константа для лучшей читаемости кода, которая обозначает, что мы пропустим 1 слово в списке
    check_zeros = 0 # Встретили ли мы 000

    i = 0 # Индекс для массива

    while i < (len(list_words)):
        if i + SKIP_WORD >= len(list_words): # Если текущее слово не с чем менять выходим
            return
        if list_words[i] == '000' and check_zeros == 0:  # Если встретили 000 первый раз(условие пригодится если 000 это первое слово в списке)
            check_zeros = 1
            i += SKIP_WORD
            continue
        if list_words[i + 1] == '000' and check_zeros == 0:  # Если встретили 000 первый раз, мы не будем менять 000 с другим словом, тк 000 наш сигнал о том, что надо менять условие
            check_zeros = 1
            i += SKIP_COUPLE_WORDS
            continue

        if check_zeros == 0:
            if i + SKIP_WORD >= len(list_words):  # Если текущее слово не с чем менять выходим
                return

            # Меняем местами слова
            current_word = list_words[i]
            list_words[i] = list_words[i + 1]
            list_words[i + 1] = current_word

            i += SKIP_COUPLE_WORDS

        if check_zeros == 1:
            if i + SKIP_COUPLE_WORDS * 3 - SKIP_WORD >= len(list_words): # Если у нас после текущей пары нет еще 3х пар слов, то продолжать не имеет смысла
                return
            i += SKIP_COUPLE_WORDS * 2  # Пропускаем 2 пары, а третью меняем

            # Меняем местами слова
            current_word = list_words[i]
            list_words[i] = list_words[i + 1]
            list_words[i + 1] = current_word
            i += 2



list_words = read()
print(list_words)
swap()

print(list_words)

