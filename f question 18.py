def find_topper(students):
    topper = students[0]
    for student in students:
        if student["marks"] > topper["marks"]:
            topper = student
    return topper["name"]

students = [
    {"name": "Amit", "marks": 85},
    {"name": "Neha", "marks": 92},
    {"name": "Ravi", "marks": 88}
]

print(find_topper(students))
