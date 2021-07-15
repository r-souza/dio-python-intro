def count_letters(words):

    counter = []

    for word in words:
        count = len(word)
        counter.append(count)

    return counter


if __name__ == '__main__':
    words = ['dog', 'horse', 'elephant']
    print(count_letters(words))
