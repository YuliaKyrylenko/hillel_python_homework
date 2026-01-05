def common_elements():
    set_3 = set()
    set_5 = set()
    for num in range(100):
        if num % 3 == 0:
            set_3.add(num)
        if num % 5 == 0:
            set_5.add(num)
    return set_3 & set_5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")