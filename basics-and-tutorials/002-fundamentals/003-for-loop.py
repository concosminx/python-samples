#for loops
friend = ["Joe", "John", "Jane"]

for f in friend:
    print(f)

#using _ signals that we do not indent to use this variable [the index] 
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for _ in elements:
    print("Hello, world!")

#using ranges
for idx in range(10):
    print("Range!")

for idx in range(2, 20, 3):
    print(str(idx))

students = [
    {"name" : "Rollo", "grade" : 10},
    {"name" : "Remy", "grade" : 8},
    {"name" : "Rully", "grade" : 6},
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")
