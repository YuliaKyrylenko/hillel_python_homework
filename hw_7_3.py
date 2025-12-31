def second_index(text, some_str):
    first_found = text.find(some_str)
    second_found = text.find(some_str, first_found + 1)
    if second_found != -1:
        return second_found
    else:
        return None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')