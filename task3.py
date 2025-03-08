# Функція для знаходження унікальних літер, що зустрічаються один раз
def unique_letters(text):
    letter_counts = {char: text.count(char) for char in set(text) if char.isalpha()}
    unique_chars = {char for char, count in letter_counts.items() if count == 1}
    print("Літери, які входять в текст один раз:", unique_chars)

# Введення тексту
text = input("Введіть текст латинськими літерами: ")
unique_letters(text)