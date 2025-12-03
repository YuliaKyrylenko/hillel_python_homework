price = float(input("Введіть ціну: "))
percent = float(input("Введіть знижку (%): "))

result = price - (price * percent / 100)
print("Ціна зі знижкою: ", result)