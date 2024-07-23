students = [
        {"name": "Alice", "age": 20, "grade": 85, "major": "Physics"},
        {"name": "Bob", "age": 22, "grade": 90, "major": "Chemistry"},
        {"name": "Charlie", "age": 19, "grade": 78, "major": "Mathematics"},
        {"name": "Diana", "age": 21, "grade": 92, "major": "Biology"}
        ]
for student in students:
    del student["age"]

for student in students:
    student["graduation_year"] = "2024"

for student in students:
    print(student)
