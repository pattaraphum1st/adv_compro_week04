numbers = [1, 2, 3, 4, 5]
modified_number = [n+10 if n % 2 == 0 else n-1 for n in numbers]
print(numbers, modified_number)
