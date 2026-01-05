def is_palindrome(text):
    from string import punctuation
    text = ''.join([letter for letter in text if letter not in punctuation])
    return text.lower().replace(' ', '') == text.lower().replace(' ', '')[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")