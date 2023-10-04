def most_frequent_word(text):
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    max_count = 0
    max_word = ''

    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count and word < max_word:
            max_word = word

    return max_word


n = int(input())
text = ''
for _ in range(n):
    text += input() + ' '

result = most_frequent_word(text)
print(result)
