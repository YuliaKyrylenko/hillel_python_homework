minutes = input("Введіть кількість хвилин: ")

result_hours = int(minutes) // 60
result_minutes = int(minutes) % 60
print(result_hours, "години", result_minutes, "хвилин")