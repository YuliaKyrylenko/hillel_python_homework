minutes = int(input("Введіть кількість хвилин: "))

result_hours, result_minutes = divmod(minutes, 60)
print(result_hours, "години", result_minutes, "хвилин")