grades = [50, 70, 65, 40, 90, 85, 50, 77]
passed_with_bonus = list(map(lambda grade: grade * 1.05, filter(lambda grade: grade >= 60, grades)))
print(passed_with_bonus)
