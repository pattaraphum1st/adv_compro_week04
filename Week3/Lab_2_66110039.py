#i=0
#while i<10:
#    i+=1
#    if i == 3:
#        continue
#    if i == 5:
#        break
#   print(i)

#numbers = [1, 2, 3, 4, 5]
#outputs = [item*2 for item in numbers]
#print(numbers, outputs)

#number = 2
#is_even = "Yes" if number % 2 == 0 else "No"
#print(is_even)

numbers = [1, 2, 3, 4, 5]
#outputs = ["Yes" if item % 2 == 0 else "No" for item in numbers]
outputs = [item for item in numbers if item % 2 == 0]
print(numbers, outputs)

