def first_word(text: str) -> str:
    """ Пошук першого слова """
    from string import punctuation
    text = text.lstrip(punctuation + " ")
    word = ""
    for letter in text:
        if letter.isalpha() or letter == "'":
            word += letter
        elif word:
            break
    return word

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')